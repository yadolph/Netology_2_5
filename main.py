

import datetime

class LogTime:
    def __init__(self, log_path, encoding='utf-8'):
        self.log_file = open(log_path, 'a', encoding=encoding)
        global start_time
        start_time = datetime.datetime.utcnow()
        self.log_file.write(f'{datetime.datetime.utcnow()}: Start \n')

    def __enter__(self):
        return self

    def write_log(self, action):
        self.log_file.write(f'{datetime.datetime.utcnow()}: {action}\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.write_log(f'error: {exc_val}')
        self.write_log('end')
        end_time = datetime.datetime.utcnow()
        complete_time = end_time - start_time

        self.write_log(f'Task completed in {complete_time} sec')
        self.log_file.close()


def count_word_wp(word):
    with LogTime('log.log') as log:
        results = []
        with open('war_and_peace1.txt') as f:
            for line in f:
                line = line.strip()
                if word in line:
                    results.append(line)
    return len(results)

user_word = input('Введите ваше слово: ')

print(f'Слово "{user_word}" встречается в первой книге романа "Война и мир" {count_word_wp(user_word)} раз')




