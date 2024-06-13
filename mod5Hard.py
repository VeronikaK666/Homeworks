# Реализовать классы для взаимодействия с платоформой, каждый из которых будет
# содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

class User:
    """
    Класс пользователя. Содержит логин, хеш пароля, возраст
    """

    def __init__(self, nickname, password, password_confirm, age):
        self.nickname = nickname
        if password == password_confirm:
            self.password = password
        self.age = age

    def __hash__(self):
        return hash((self.password, self.password_confirm))

    def __str__(self):
        return self.nickname

    pass


class Video:
    """
    Класс видео
    Атрибуты:
    title(заголовок, строка),
    duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    pass

class UrTube:
    """
    Класс интернет-платформы университета Urban,
    где будут размещаться дополнительные полезные ролики на тему IT.
    Содержит список пользователей, список видео, текущего пользователя
    и методы работы с ними
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, nickname=None, video=None, password=None):
        """
        Метод проверяет? существует ли пользователь или видео в базе
        nickname: пользователь для проверки
        video: видео для проверки
        :return: номер позиции +1, либо 0, в случае, если ничего не найдено
        """
        if nickname == None:
            if video == None:
                return False
            else:
                for i in range(len(self.videos)):
                    if str(self.videos[i].title).upper() == video.upper():
                        return i + 1
                return 0

        else:
            for i in range(len(self.users)):
                if str(self.users[i]) == nickname:
                    if password is None:
                        return i + 1
                    if self.users[i].password == password:
                        return i + 1
                    else:
                        return 0
            return 0

    def log_in(self, login, password):
        self.login = login
        self.password = password
        """
        Вход пользователя в систему
        login: Имя пользователя
        password: Хеш пароля
        """

        bool_ = self.__contains__(login, password)
        if bool_:
            print(f'\nВы вошли как {login}')
            self.current_user = self.users[bool_ - 1]
        else:
            print('\nНеверный логин или пароль. Вход не выполнен.')


    def register(self, nickname, password, password_confirm, age):
        """
        Регистрация пользователя в системе
        nickname: Имя пользователя
        password: Пароль
        password_confirm: Повторный ввод пароля
        age: Возраст
        :return: Ничего не dозвращает
        """
        if nickname not in self:
            if password == password_confirm:
                self.users += [User(nickname, password, password_confirm, age)]
                self.log_in(nickname, password)
            else:
                print('\nПароли не совпадают, попробуйте ещё раз.')
        else:
            print(f'\nПользователь {nickname} уже существует')

    def log_out(self):
        """
        Выход из системы
        сброс текущего пользователя на None
        """
        self.current_user = None

    def add(self, *video):
        """
        Метод добавляет неограниченное количество видео
        video: список объектов класса Video
        :return: Ничего не возвращает
        """
        for vid_ in video:
            if self.__contains__(video=vid_.title):
                print(f'Видео с таким названием {vid_.title} уже существует.')
            else:
                self.videos += [vid_]

    def get_videos(self, video):
        """
        Метод get_videos принимает поисковое слово и возвращает список названий
        всех видео, содержащих поисковое слово. Регистр не учитывается.
        video: Слово для поиска
        :return: Список названий всех видео
        """
        res = []
        for i in self.videos:
            if video.upper() in str(i.title).upper():
                res += [i.title]
        return res

    def watch_video(self, video):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения
        (вплоть до пробела), то ничего не воспроизводится, если же находит, ведётся отчёт в консоль
        на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
        video: Название видео
        :return: Ничего не возвращает
        """


        if ur.current_user == None:
            print('\nВойдите в аккаунт, чтобы смотреть видео')
            return


        bool_ = self.__contains__(video=video)
        if bool_:
            if self.videos[bool_ - 1].adult_mode and self.current_user.age < 18:
                print('\nВам нет 18 лет, пожалуйста, покиньте страницу')
                return
        else:
            print(f'\nТакого видео "{video}" не существует.')
            return


        print(f'\nПросмотр видео "{video}" начался:')
        for i in range(self.videos[bool_ - 1].time_now, self.videos[bool_ - 1].duration + 1):
            print(i, end=' ')

            return
        print('Конец видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', hash('lolkekcheburek'), hash('lolkekcheburek'), 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', hash('iScX4vIJClb9YQavjAgF'), hash('iScX4vIJClb9YQavjAgF'), 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', hash('F8098FM8fjm9jmi'), hash('F8098FM8fjm9jmi'), 55)

    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
    pass

