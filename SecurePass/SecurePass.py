import random
import string
import pyperclip

translations = {
    'en': {
        'welcome_message': 'Welcome to the Password Generator!\n[+] Enter -> Yes\n[+] (-) -> No\n',
        'enter_password_length': 'Enter the password length: ',
        'generate_single_password': 'Generate a single password (Enter) or multiple passwords (-)? ',
        'use_lowercase': 'Use lowercase letters?',
        'use_uppercase': 'Use uppercase letters?',
        'use_digits': 'Use digits? (press Enter/-) ',
        'use_special_chars': 'Use special characters?',
        'use_time_factor': 'Use time factor?',
        'safe_password': 'Your secure password: ',
        'password_copied': 'Password copied to clipboard.',
        'enter_num_passwords': 'Enter the number of passwords to generate: ',
        'passwords_saved': 'Passwords saved in file: p1ass.txt',
        'invalid_input': 'Error: Invalid input.',
        'error_occurred': 'An error occurred: ',
        'press_enter': 'Press Enter to exit.',
    },
    'ru': {
        'welcome_message': 'Добро пожаловать в генератор паролей!   \n[+] Enter -> Да  \n[+] (-) -> Нет \n',
        'enter_password_length': 'Введите длину пароля: ',
        'generate_single_password': 'Сгенерировать один пароль (Enter) или несколько паролей (-)? ',
        'use_lowercase': 'Использовать строчные буквы?',
        'use_uppercase': 'Использовать заглавные буквы?',
        'use_digits': 'Использовать цифры? (нажмите Enter/-) ',
        'use_special_chars': 'Использовать специальные символы?',
        'use_time_factor': 'Использовать фактор времени?',
        'safe_password': 'Ваш безопасный пароль: ',
        'password_copied': 'Пароль скопирован в буфер обмена.',
        'enter_num_passwords': 'Введите количество генерируемых паролей: ',
        'passwords_saved': 'Пароли сохранены в файле: p1ass.txt',
        'invalid_input': 'Ошибка: некорректный ввод.',
        'error_occurred': 'Произошла ошибка: ',
        'press_enter': 'Нажмите Enter для выхода.',
    },
    'fr': {
        'welcome_message': 'Bienvenue dans le générateur de mots de passe !\n[+] Enter -> Oui\n[+] (-) -> Non\n',
        'enter_password_length': 'Entrez la longueur du mot de passe : ',
        'generate_single_password': 'Générer un seul mot de passe (Enter) ou plusieurs mots de passe (-) ? ',
        'use_lowercase': 'Utiliser des lettres minuscules ?',
        'use_uppercase': 'Utiliser des lettres majuscules ?',
        'use_digits': 'Utiliser des chiffres ? (appuyez sur Enter/-) ',
        'use_special_chars': 'Utiliser des caractères spéciaux ?',
        'use_time_factor': 'Utiliser un facteur temps ?',
        'safe_password': 'Votre mot de passe sécurisé : ',
        'password_copied': 'Mot de passe copié dans le presse-papiers.',
        'enter_num_passwords': 'Entrez le nombre de mots de passe à générer : ',
        'passwords_saved': 'Mots de passe enregistrés dans le fichier : p1ass.txt',
        'invalid_input': 'Erreur : Entrée invalide.',
        'error_occurred': 'Une erreur s\'est produite : ',
        'press_enter': 'Appuyez sur Enter pour quitter.',
    },
    'es': {
        'welcome_message': '¡Bienvenido al Generador de Contraseñas!\n[+] Enter -> Sí\n[+] (-) -> No\n',
        'enter_password_length': 'Ingrese la longitud de la contraseña: ',
        'generate_single_password': 'Generar una sola contraseña (Enter) o varias contraseñas (-)? ',
        'use_lowercase': 'Usar letras minúsculas?',
        'use_uppercase': 'Usar letras mayúsculas?',
        'use_digits': 'Usar dígitos? (presione Enter/-) ',
        'use_special_chars': 'Usar caracteres especiales?',
        'use_time_factor': 'Usar factor de tiempo?',
        'safe_password': 'Su contraseña segura: ',
        'password_copied': 'Contraseña copiada al portapapeles.',
        'enter_num_passwords': 'Ingrese la cantidad de contraseñas a generar: ',
        'passwords_saved': 'Contraseñas guardadas en el archivo: p1ass.txt',
        'invalid_input': 'Error: Entrada inválida.',
        'error_occurred': 'Se produjo un error: ',
        'press_enter': 'Presione Enter para salir.',
    },
    'de': {
        'welcome_message': 'Willkommen beim Passwortgenerator!\n[+] Enter -> Ja\n[+] (-) -> Nein\n',
        'enter_password_length': 'Geben Sie die Passwortlänge ein: ',
        'generate_single_password': 'Einzelnes Passwort generieren (Enter) oder mehrere Passwörter (-)? ',
        'use_lowercase': 'Kleinbuchstaben verwenden?',
        'use_uppercase': 'Großbuchstaben verwenden?',
        'use_digits': 'Zahlen verwenden? (Enter/- drücken) ',
        'use_special_chars': 'Sonderzeichen verwenden?',
        'use_time_factor': 'Zeitfaktor verwenden?',
        'safe_password': 'Ihr sicheres Passwort: ',
        'password_copied': 'Passwort in die Zwischenablage kopiert.',
        'enter_num_passwords': 'Geben Sie die Anzahl der zu generierenden Passwörter ein: ',
        'passwords_saved': 'Passwörter wurden in der Datei p1ass.txt gespeichert.',
        'invalid_input': 'Fehler: Ungültige Eingabe.',
        'error_occurred': 'Ein Fehler ist aufgetreten: ',
        'press_enter': 'Drücken Sie Enter, um zu beenden.',
    },
    'it': {
        'welcome_message': 'Benvenuto nel Generatore di Password!\n[+] Enter -> Sì\n[+] (-) -> No\n',
        'enter_password_length': 'Inserisci la lunghezza della password: ',
        'generate_single_password': 'Generare una singola password (Enter) o più password (-)? ',
        'use_lowercase': 'Usare lettere minuscole?',
        'use_uppercase': 'Usare lettere maiuscole?',
        'use_digits': 'Usare cifre? (premere Enter/-) ',
        'use_special_chars': 'Usare caratteri speciali?',
        'use_time_factor': 'Usare il fattore tempo?',
        'safe_password': 'La tua password sicura: ',
        'password_copied': 'Password copiata negli appunti.',
        'enter_num_passwords': 'Inserisci il numero di password da generare: ',
        'passwords_saved': 'Password salvate nel file: p1ass.txt',
        'invalid_input': 'Errore: Input non valido.',
        'error_occurred': 'Si è verificato un errore: ',
        'press_enter': 'Premi Enter per uscire.',
    },
    'pt': {
        'welcome_message': 'Bem-vindo ao Gerador de Senhas!\n[+] Enter -> Sim\n[+] (-) -> Não\n',
        'enter_password_length': 'Digite o comprimento da senha: ',
        'generate_single_password': 'Gerar uma única senha (Enter) ou várias senhas (-)? ',
        'use_lowercase': 'Usar letras minúsculas?',
        'use_uppercase': 'Usar letras maiúsculas?',
        'use_digits': 'Usar dígitos? (pressione Enter/-) ',
        'use_special_chars': 'Usar caracteres especiais?',
        'use_time_factor': 'Usar fator de tempo?',
        'safe_password': 'Sua senha segura: ',
        'password_copied': 'Senha copiada para a área de transferência.',
        'enter_num_passwords': 'Digite o número de senhas a serem geradas: ',
        'passwords_saved': 'Senhas salvas no arquivo: p1ass.txt',
        'invalid_input': 'Erro: Entrada inválida.',
        'error_occurred': 'Ocorreu um erro: ',
        'press_enter': 'Pressione Enter para sair.',
    },
    'zh': {
        'welcome_message': '欢迎使用密码生成器！\n[+] Enter -> 是\n[+] (-) -> 否\n',
        'enter_password_length': '输入密码长度：',
        'generate_single_password': '生成单个密码（Enter）还是多个密码（-）？',
        'use_lowercase': '使用小写字母？',
        'use_uppercase': '使用大写字母？',
        'use_digits': '使用数字？（按Enter/-）',
        'use_special_chars': '使用特殊字符？',
        'use_time_factor': '使用时间因素？',
        'safe_password': '您的安全密码：',
        'password_copied': '密码已复制到剪贴板。',
        'enter_num_passwords': '输入要生成的密码数量：',
        'passwords_saved': '密码已保存在文件p1ass.txt中。',
        'invalid_input': '错误：无效的输入。',
        'error_occurred': '发生错误：',
        'press_enter': '按Enter键退出。',
    },
    'ja': {
        'welcome_message': 'パスワードジェネレータへようこそ！\n[+] Enter -> はい\n[+] (-) -> いいえ\n',
        'enter_password_length': 'パスワードの長さを入力してください：',
        'generate_single_password': '単一のパスワードを生成しますか（Enter）それとも複数のパスワードを生成しますか（-）？',
        'use_lowercase': '小文字を使用しますか？',
        'use_uppercase': '大文字を使用しますか？',
        'use_digits': '数字を使用しますか？（Enter/- を押してください）',
        'use_special_chars': '特殊文字を使用しますか？',
        'use_time_factor': '時間要素を使用しますか？',
        'safe_password': '安全なパスワード：',
        'password_copied': 'パスワードがクリップボードにコピーされました。',
        'enter_num_passwords': '生成するパスワードの数を入力してください：',
        'passwords_saved': 'パスワードはp1ass.txtファイルに保存されました。',
        'invalid_input': 'エラー：無効な入力です。',
        'error_occurred': 'エラーが発生しました：',
        'press_enter': '終了するにはEnterキーを押してください。',
    },
    'ko': {
        'welcome_message': '비밀번호 생성기에 오신 것을 환영합니다!\n[+] Enter -> 예\n[+] (-) -> 아니요\n',
        'enter_password_length': '비밀번호 길이를 입력하세요: ',
        'generate_single_password': '단일 비밀번호 생성 (Enter) 또는 다중 비밀번호 생성 (-)? ',
        'use_lowercase': '소문자 사용?',
        'use_uppercase': '대문자 사용?',
        'use_digits': '숫자 사용? (Enter/- 입력) ',
        'use_special_chars': '특수 문자 사용?',
        'use_time_factor': '시간 요소 사용?',
        'safe_password': '안전한 비밀번호: ',
        'password_copied': '비밀번호가 클립보드에 복사되었습니다.',
        'enter_num_passwords': '생성할 비밀번호 수를 입력하세요: ',
        'passwords_saved': '비밀번호가 p1ass.txt 파일에 저장되었습니다.',
        'invalid_input': '오류: 잘못된 입력입니다.',
        'error_occurred': '오류가 발생했습니다: ',
        'press_enter': '종료하려면 Enter를 누르세요.',
    },
    'ar': {
        'welcome_message': 'مرحبًا بك في مولد كلمات المرور!\n[+] Enter -> نعم\n[+] (-) -> لا\n',
        'enter_password_length': 'أدخل طول كلمة المرور: ',
        'generate_single_password': 'توليد كلمة مرور واحدة (Enter) أو عدة كلمات مرور (-)؟ ',
        'use_lowercase': 'استخدام الأحرف الصغيرة؟',
        'use_uppercase': 'استخدام الأحرف الكبيرة؟',
        'use_digits': 'استخدام الأرقام؟ (اضغط Enter/-) ',
        'use_special_chars': 'استخدام الرموز الخاصة؟',
        'use_time_factor': 'استخدام عامل الوقت؟',
        'safe_password': 'كلمة المرور الآمنة الخاصة بك: ',
        'password_copied': 'تم نسخ كلمة المرور إلى الحافظة.',
        'enter_num_passwords': 'أدخل عدد كلمات المرور المراد توليدها: ',
        'passwords_saved': 'تم حفظ كلمات المرور في الملف: p1ass.txt',
        'invalid_input': 'خطأ: إدخال غير صالح.',
        'error_occurred': 'حدث خطأ: ',
        'press_enter': 'اضغط على Enter للخروج.',
    },
    'tr': {
        'welcome_message': 'Parola Oluşturucuya Hoş Geldiniz!\n[+] Enter -> Evet\n[+] (-) -> Hayır\n',
        'enter_password_length': 'Parola uzunluğunu girin: ',
        'generate_single_password': 'Tek bir parola oluştur (Enter) veya birden fazla parola oluştur (-)? ',
        'use_lowercase': 'Küçük harfleri kullan?', 'use_uppercase': 'Büyük harfleri kullan?',
        'use_digits': 'Rakamları kullan? (Enter/- tuşuna basın) ',
        'use_special_chars': 'Özel karakterleri kullan?',
        'use_time_factor': 'Zaman faktörünü kullan?',
        'safe_password': 'Güvenli parolanız: ',
        'password_copied': 'Parola panoya kopyalandı.',
        'enter_num_passwords': 'Oluşturulacak parola sayısını girin: ',
        'passwords_saved': 'Parolalar p1ass.txt dosyasına kaydedildi.',
        'invalid_input': 'Hata: Geçersiz giriş.',
        'error_occurred': 'Bir hata oluştu: ',
        'press_enter': 'Çıkmak için Enter tuşuna basın.',
    },
    'fr': {
        'welcome_message': 'Bienvenue dans le générateur de mots de passe !\n[+] Enter -> Oui\n[+] (-) -> Non\n',
        'enter_password_length': 'Entrez la longueur du mot de passe : ',
        'generate_single_password': 'Générer un seul mot de passe (Enter) ou plusieurs mots de passe (-) ? ',
        'use_lowercase': 'Utiliser des minuscules ?',
        'use_uppercase': 'Utiliser des majuscules ?',
        'use_digits': 'Utiliser des chiffres ? (appuyez sur Enter/-) ',
        'use_special_chars': 'Utiliser des caractères spéciaux ?',
        'use_time_factor': 'Utiliser un facteur temps ?',
        'safe_password': 'Votre mot de passe sécurisé : ',
        'password_copied': 'Mot de passe copié dans le presse-papiers.',
        'enter_num_passwords': 'Entrez le nombre de mots de passe à générer : ',
        'passwords_saved': 'Mots de passe enregistrés dans le fichier p1ass.txt.',
        'invalid_input': 'Erreur : Entrée invalide.',
        'error_occurred': 'Une erreur est survenue : ',
        'press_enter': 'Appuyez sur Entrée pour quitter.',
    },
    'pl': {
        'welcome_message': 'Witaj w generatorze haseł! \n[+] Enter -> Tak \n[+] (-) -> Nie \n',
        'enter_password_length': 'Podaj długość hasła: ',
        'generate_single_password': 'Wygenerować pojedyncze hasło (Enter) czy kilka haseł (-)? ',
        'use_lowercase': 'Używać małych liter?',
        'use_uppercase': 'Używać dużych liter?',
        'use_digits': 'Używać cyfr? (naciśnij Enter/-) ',
        'use_special_chars': 'Używać znaków specjalnych?',
        'use_time_factor': 'Używać czynnika czasu?',
        'safe_password': 'Twoje bezpieczne hasło: ',
        'password_copied': 'Hasło skopiowane do schowka.',
        'enter_num_passwords': 'Podaj liczbę generowanych haseł: ',
        'passwords_saved': 'Hasła zapisane w pliku: p1ass.txt',
        'invalid_input': 'Błąd: nieprawidłowe dane wejściowe.',
        'error_occurred': 'Wystąpił błąd: ',
        'press_enter': 'Naciśnij Enter, aby zakończyć.',
}
}

def translate(text, language):
    if language in translations and text in translations[language]:
        return translations[language][text]
    else:
        return translations['en'][text] if 'en' in translations and text in translations['en'] else text

def translated_input(prompt, language):
    translated_prompt = translate(prompt, language)
    return input(translated_prompt)

def translated_print(text, language):
    translated_text = translate(text, language)
    print(translated_text)

def generate_password(length=8, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input(language):
    length = int(translated_input('enter_password_length', language))
    single_password = translated_input('generate_single_password', language)
    use_lowercase = translated_input('use_lowercase', language)
    use_uppercase = translated_input('use_uppercase', language)
    use_digits = translated_input('use_digits', language)
    use_special_chars = translated_input('use_special_chars', language)
    use_time_factor = translated_input('use_time_factor', language)
    return length, single_password, use_lowercase, use_uppercase, use_digits, use_special_chars, use_time_factor

def save_passwords(passwords):
    with open("p1ass.txt", "a") as file:
        for password in passwords:
            file.write(password + "\n")

def main():
    system_language = 'ru'  # Set the desired language here

    translated_print('welcome_message', system_language)

    try:
        length, single_password, use_lowercase, use_uppercase, use_digits, use_special_chars, use_time_factor = get_user_input(system_language)

        single_password = True if single_password == '' else False
        use_lowercase = True if use_lowercase == '' else False
        use_uppercase = True if use_uppercase == '' else False
        use_digits = True if use_digits == '' else False
        use_special_chars = True if use_special_chars == '' else False
        use_time_factor = True if use_time_factor == '' else False

        passwords = []
        if single_password:
            password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
            passwords.append(password)
            pyperclip.copy(password)
            translated_print('safe_password', system_language)
            print(password)
            translated_print('password_copied', system_language)
        else:
            num_passwords = int(translated_input('enter_num_passwords', system_language))
            for _ in range(num_passwords):
                if use_time_factor:
                    length = length - 4  # Subtract 4 characters for time factor
                password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
                if use_time_factor:
                    time_factor = str(int(time.time()))[-4:]  # Get last 4 digits of current time
                    password += time_factor
                passwords.append(password)
                print(password)

        save_passwords(passwords)
        translated_print('passwords_saved', system_language)

    except ValueError:
        translated_print('invalid_input', system_language)
    except Exception as e:
        translated_print('error_occurred', system_language)
        print(str(e))

    translated_input('press_enter', system_language)

if __name__ == "__main__":
    main()
