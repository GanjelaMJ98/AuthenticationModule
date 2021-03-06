# AuthenticationModule

Определения и сокращения

Аутентификация - проверка подлинности предъявленного пользователем идентификатора.

Авторизация - предоставление определённому лицу или группе лиц прав на выполнение
определённых действий; а также процесс проверки (подтверждения) данных прав при попытке
выполнения этих действий

N – счетчик попыток входа в систему
ЖБ – журнал безопасности, см. в соответствующих документах
МКД – модуль контроля доступа
УЗ – учетная запись
ОП – основная программа


Вызов МКД происходит из ОП.

Так же МКД получает от ОП пути расположений файлов УЗ и ЖБ и открывает их для
чтения/записи.

После вызова МКД, отображается форма ввода пользователя и пароля.

При нажатии на кнопку “Войти”, МКД сличает введенные данные с записями в файле:

- “Имя пользователя” и “Пароль” валидны:
		o Отправить соответствующую запись в ЖБ (дата и время, имя пользователя) о
		входе в систему
		o Передать имя пользователя и флаг привилегии в основную программу
- else
		o Отправить запись в ЖБ (дата и время, имя пользователя) о неудачной попытке
		входа
		o Вывести на экран сообщение о неверном логине или пароле
		o Повторный ввод “Имени пользователя” и “пароля” (при N =&gt; 3, закрыть
		основную программу)

Предусмотреть checkbox с возможностью отображения введённого пароля
Так же необходимо обеспечить скрытие символов вводимого пароля.

Файл УЗ содержит:

- Имя пользователя
- Пароль
- Флаг привилегий

Флаги привилегий:

- a – администратор
- m – модератор
- o – оператор