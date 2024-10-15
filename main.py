# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
# Метод log_out для сброса текущего пользователя на None.
# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"
from time import sleep


class User:

    def __init__(self, nickname: str, password: str, age: int):

        self.nickname: str = nickname
        self.password: str = password
        self.age: int = age

    def __eq__(self, other):

        if self.nickname == other.nickname and self.password == other.password:
            return True


class Video:

    def __init__(self, title: str, duration: int, time_now: int, adult_mode: bool = False):

        self.title: str = title
        self.duration: int = duration
        self.time_now: int = time_now
        self.adult_mode: bool = adult_mode

    def __eq__(self, other):

        if self.title == other.title:

            return True


class UrTube:

    def __init__(self):

        self.users: list[User] = []
        self.videos: list[Video] = []
        self.current_user: User = None

    def log_in(self, nickname: str, password: str) -> User:

        for user in self.users:

            if user.nickname == nickname and user.password == password:

                print(f'<{user.nickname}> успешно авторизовался!')
                self.current_user = user
                return user

        print(f'Не верно введен логин или пароль! Либо Вы не зарегистрированы!')
        return None

    def register(self, nickname: str, password: str, age: int) -> User:

        newUser = User(nickname, password, age)

        for user in self.users:

            if user == newUser:
                print(f'Пользователь с таким логином уже зарегистрирован!')
                return None

        print(f'<{newUser.nickname}> был зарегистрирован успешно!')
        self.users += [newUser]
        return newUser

    def log_out(self) -> None:
        self.current_user = None

    def add(self, newVideos: list[Video]) -> None:

        for video in newVideos:
            if video not in self.videos:
                print(f'Видео: <{video.title}> было добавлено на сайт!')
                self.videos += [video]
            else:
                print(f'Такое видео уже существует!')

    def __get_videos(self, title: str) -> list[Video]:

        videos: list[Video] = []

        for video in self.videos:

            if title.lower() in video.title.lower():
                videos += [video]

        return videos

    def watch_video(self, videoTitle: str) -> None:

        if self.current_user is None:
            print('Войдите в свой аккаунт для просмотра видео')
            return

        videos: list[Video] = self.__get_videos(videoTitle)

        if videos.__len__() > 0:

            for video in videos:

                if video.adult_mode and self.current_user.age < 18:
                    print(f'Вам нет 18 лет, видео <{video.title}> для Вас недоступно')
                    return
                else:

                    for watchingTime in range(video.time_now, video.duration):
                        sleep(1)
                        print(f'Смотрим видео <{watchingTime}> секунда')

                    print('Видео просмотрено')

        else:
            print(f'По Вашему запросу <{videoTitle}> не найдено ни одного видео!')





ut = UrTube()
ut.register('Alex', '123', 17)
ut.register('Alex', '123', 33)
ut.log_in('Alex', '1234')
ut.log_in('Alex', '123')
ut.add([Video('Видео1', 5, 0, False), Video('Видео2', 10, 0, True)])
ut.watch_video('Видео')