from time import sleep
class User:
    def __init__(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age

    def __repr__(self):
        return f'{self.name}'


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title and self.adult_mode == other.adult_mode
        return False

    def __hash__(self):
        return hash(self.title)

    def __repr__(self):
        return f'{self.title}'


class UrTube:
    def __init__(self):
        self.users = {}
        self.video = set()
        self.current_user = None

    def __repr__(self):
        return f'{self.users}, видео: {self.video}, текущий пользователь: {self.current_user}'

    def add(self, *video):
        for i in video:
            self.video.add(i)

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует.')
        else:
            self.users[nickname] = User(nickname, hash(str(password)), age)
            self.log_in(nickname, password)

    def log_in(self, nickname, password):
        if nickname in self.users:
            user = self.users[nickname]
            if user.password == hash(str(password)):
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def watch_video(self, videos):
        if self.current_user is not None:
            for i in self.video:
                if i.title == videos:
                    if i.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу"')
                    else:
                        for k in range(i.duration):
                            print(f'{k+1}')
                            sleep(1)
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def get_videos(self, wath_word):
        list_video = []
        for i in self.video:
            if wath_word.lower() in i.title.lower():
                list_video.append(str(i))
        return list_video


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
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
