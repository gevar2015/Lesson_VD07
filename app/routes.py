from flask import render_template, request, flash, redirect, url_for
from app import app

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Проверяем введенные данные (упрощенная проверка)
        if not name or not email or not password:
            flash('All fields are required!', 'danger')
        else:
            # Здесь может быть логика сохранения данных в базу данных
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('edit_profile'))

    # Рендерим шаблон, передавая текущие данные пользователя (здесь просто пример значений)
    return render_template('edit_profile.html', name='John Doe', email='john.doe@example.com')
