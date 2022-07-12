from time import sleep


def main():
    def decorator(call_count=4, start_sleep_time=3, factor=3, border_sleep_time=100):

        def wrapper(func):

            def inner():
                t = start_sleep_time
                print(f'Кол-во запусков = {call_count}\nНачало работы')
                for i in range(1, call_count + 1):
                    sleep(t)
                    func_result = func()
                    print(f'Запуск номер {i}. Ожидание: {t} секунд. Результат декорируемой функций = {func_result}.')
                    t = t * 2 ** factor if t * 2 ** factor < border_sleep_time else border_sleep_time
                    if i == call_count:
                        print('Конец работы')

            return inner

        return wrapper

    @decorator(call_count=3, start_sleep_time=2, factor=2, border_sleep_time=33)
    def function():
        return 'function()'

    function()

if __name__ == '__main__':
    main()
