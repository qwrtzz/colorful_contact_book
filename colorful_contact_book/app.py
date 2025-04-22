import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk # type: ignore
from database import SessionLocal, Contact
import re

# Глобальные переменные для сортировки
sort_column = "name"  # По умолчанию сортируем по имени
sort_order = "ASC"
column_map = {
    "id": Contact.id,
    "name": Contact.name,
    "phone": Contact.phone,
    "email": Contact.email,
    "category": Contact.category
}

def load_contacts():
    # Обновляем список категорий
    db = SessionLocal()
    all_categories = db.query(Contact.category).distinct().all()
    all_categories = ["All"] + [cat[0] for cat in all_categories]
    category_filter_combo['values'] = all_categories
    # Проверяем, если текущая категория фильтра не валидна, сбрасываем на "All"
    if category_filter_combo.get() not in all_categories:
        category_filter_combo.set("All")
    
    # Получаем текущие фильтры из интерфейса
    search_term = search_entry.get()
    category_filter = category_filter_combo.get()
    
    # Очищаем таблицу
    for item in tree.get_children():
        tree.delete(item)
    
    # Создаем запрос
    query = db.query(Contact)
    if search_term:
        query = query.filter(
            (Contact.name.like(f"%{search_term}%")) |
            (Contact.phone.like(f"%{search_term}%")) |
            (Contact.email.like(f"%{search_term}%"))
        )
    if category_filter != "All":
        query = query.filter(Contact.category == category_filter)
    if sort_column:
        attr = column_map.get(sort_column)
        if attr:
            if sort_order == "ASC":
                query = query.order_by(attr)
            else:
                query = query.order_by(attr.desc())
    contacts = query.all()
    
    # Заполняем таблицу
    for contact in contacts:
        tree.insert("", "end", values=(contact.id, contact.name, contact.phone, contact.email, contact.category), tags=(contact.category,))
    
    db.close()

def on_column_click(column):
    global sort_column, sort_order
    if sort_column == column:
        sort_order = "DESC" if sort_order == "ASC" else "ASC"
    else:
        sort_column = column
        sort_order = "ASC"
    load_contacts()

def open_contact_form(name="", phone="", email="", category="Friends", contact_id=None):
    form = tk.Toplevel(root)
    form.title("Add Contact" if contact_id is None else "Edit Contact")
    form.geometry("300x200")

    ttk.Label(form, text="Name:").grid(row=0, column=0, padx=5, pady=5)
    name_entry = ttk.Entry(form)
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    name_entry.insert(0, name)

    ttk.Label(form, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
    phone_entry = ttk.Entry(form)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)
    phone_entry.insert(0, phone)

    ttk.Label(form, text="Email:").grid(row=2, column=0, padx=5, pady=5)
    email_entry = ttk.Entry(form)
    email_entry.grid(row=2, column=1, padx=5, pady=5)
    email_entry.insert(0, email)

    ttk.Label(form, text="Category:").grid(row=3, column=0, padx=5, pady=5)
    category_combo = ttk.Combobox(form, values=["Family", "Work", "Friends", "Other"])
    category_combo.grid(row=3, column=1, padx=5, pady=5)
    category_combo.set(category)

    def save():
        new_name = name_entry.get()
        if not new_name:
            messagebox.showerror("Error", "Name is required")
            return
        new_phone = phone_entry.get()
        new_email = email_entry.get()
        if new_email and not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            messagebox.showerror("Error", "Invalid email format")
            return
        new_category = category_combo.get()
        if not new_category:
            messagebox.showerror("Error", "Category is required")
            return
        db = SessionLocal()
        if contact_id is None:
            new_contact = Contact(name=new_name, phone=new_phone, email=new_email, category=new_category)
            db.add(new_contact)
        else:
            db.query(Contact).filter(Contact.id == contact_id).update({
                Contact.name: new_name,
                Contact.phone: new_phone,
                Contact.email: new_email,
                Contact.category: new_category
            })
        db.commit()
        db.close()
        form.destroy()
        load_contacts()

    ttk.Button(form, text="Save", command=save).grid(row=4, column=0, columnspan=2, pady=10)

def add_contact():
    open_contact_form()

def edit_contact():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "No contact selected")
        return
    item = tree.item(selected[0])
    contact_id = item["values"][0]
    name = item["values"][1]
    phone = item["values"][2]
    email = item["values"][3]
    category = item["values"][4]
    open_contact_form(name, phone, email, category, contact_id)

def delete_contact():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "No contact selected")
        return
    item = tree.item(selected[0])
    contact_id = item["values"][0]
    if messagebox.askyesno("Confirm", "Are you sure you want to delete this contact?"):
        db = SessionLocal()
        db.query(Contact).filter(Contact.id == contact_id).delete()
        db.commit()
        db.close()
        load_contacts()

# Основное окно приложения
root = ThemedTk(theme="arc")
root.title("Colorful Contact Book")
root.geometry("800x600")

# Фрейм для поиска
search_frame = ttk.Frame(root)
search_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
ttk.Label(search_frame, text="Search:").grid(row=0, column=0)
search_entry = ttk.Entry(search_frame)
search_entry.grid(row=0, column=1)
search_button = ttk.Button(search_frame, text="Search", command=load_contacts)
search_button.grid(row=0, column=2)
ttk.Label(search_frame, text="Category:").grid(row=0, column=3)
category_filter_combo = ttk.Combobox(search_frame, values=["All"])
category_filter_combo.grid(row=0, column=4)
category_filter_combo.set("All")
category_filter_combo.bind("<<ComboboxSelected>>", lambda event: load_contacts())

# Фрейм для таблицы
tree_frame = ttk.Frame(root)
tree_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
tree = ttk.Treeview(tree_frame, columns=("id", "name", "phone", "email", "category"), show="headings")
tree.heading("id", text="ID", command=lambda: on_column_click("id"))
tree.heading("name", text="Name", command=lambda: on_column_click("name"))
tree.heading("phone", text="Phone", command=lambda: on_column_click("phone"))
tree.heading("email", text="Email", command=lambda: on_column_click("email"))
tree.heading("category", text="Category", command=lambda: on_column_click("category"))
tree.column("id", width=0, stretch=tk.NO)  # Скрываем столбец ID
tree.column("name", width=150)
tree.column("phone", width=100)
tree.column("email", width=150)
tree.column("category", width=100)
tree.pack(side="left", fill="both", expand=True)
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Настройка цветов для категорий
tree.tag_configure("Family", background="lightblue")
tree.tag_configure("Work", background="lightgreen")
tree.tag_configure("Friends", background="lightcoral")
tree.tag_configure("Other", background="lightgray")

# Фрейм для кнопок
buttons_frame = ttk.Frame(root)
buttons_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
add_button = ttk.Button(buttons_frame, text="Add", command=add_contact)
add_button.grid(row=0, column=0, padx=5)
edit_button = ttk.Button(buttons_frame, text="Edit", command=edit_contact)
edit_button.grid(row=0, column=1, padx=5)
delete_button = ttk.Button(buttons_frame, text="Delete", command=delete_contact)
delete_button.grid(row=0, column=2, padx=5)

# Настройка сетки
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Загрузка контактов при запуске
load_contacts()

root.mainloop()