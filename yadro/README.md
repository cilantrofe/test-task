# Тестовое задание

## Описание

Небольшая программа для обработки событий и подсчёта выручки.

## Сборка и запуск

1. Сначала склонируйте репозиторий на локальную машину:
```bash
    git clone https://github.com/cilantrofe/TEST_TASK.git
    cd TEST_TASK
```

### Linux
2. Соберите проект:
```bash
    cmake -Bbuild
    cd build
    make
```
3. Запустите, указав файл с входными данными:
```bash
    ./computer_club ../data/1.txt
```

### Windows
2. Соберите проект с помощью **Cygwin**:
```bash
    cmake -Bbuild -G "Unix Makefiles"
    cd build
    make
```
3. Запустите, указав файл с входными данными:
```bash
    .\computer_club.exe ..\data\2.txt
```

## Тестовые примеры

### №1.

### Входной файл:

```bash
    3
    09:00 19:00
    10
    08:48 1 client1
    09:41 1 client1
    09:48 1 client2
    09:52 3 client1
    09:54 2 client1 1
    10:25 2 client2 2
    10:58 1 client3
    10:59 2 client3 3
    11:30 1 client4
    11:35 2 client4 2
    11:45 3 client4
    12:33 4 client1
    12:43 4 client2
    15:52 4 client4
```

### Вывод в консоль:
```bash
    09:00
    08:48 1 client1
    08:48 13 NotOpenYet
    09:41 1 client1
    09:48 1 client2
    09:52 3 client1
    09:52 13 ICanWaitNoLonger!
    09:54 2 client1 1
    10:25 2 client2 2
    10:58 1 client3
    10:59 2 client3 3
    11:30 1 client4
    11:35 2 client4 2
    11:35 13 PlaceIsBusy
    11:45 3 client4
    12:33 4 client1
    12:33 12 client4 1
    12:43 4 client2
    15:52 4 client4
    19:00 11 client3
    19:00
    1 70 05:58
    2 30 02:18
    3 90 08:01
```

### №2.

### Входной файл:

```bash
    3
    08:00 15:00
    18
    08:00 1 ab1
    08:01 2 ab1 2
    09:03 1 ab1
    09:08 1 aa2
    09:08 2 aa2 2
    09:08 3 aa2
    09:08 2 aa2 1
    14:00 2 aab 1
    14:01 1 aab
    14:02 1 aab3
    14:02 2 aab3 3
```

### Вывод в консоль:
```bash
    08:00
    08:00 1 ab1
    08:01 2 ab1 2
    09:03 1 ab1
    09:03 13 YouShallNotPass  
    09:08 1 aa2
    09:08 2 aa2 2
    09:08 13 PlaceIsBusy      
    09:08 3 aa2
    09:08 13 ICanWaitNoLonger!
    09:08 2 aa2 1
    14:00 2 aab 1
    14:00 13 ClientUnknown    
    14:01 1 aab
    14:02 1 aab3
    14:02 2 aab3 3
    15:00 11 aa2
    15:00 11 aab
    15:00 11 aab3
    15:00 11 ab1
    15:00
    1 108 05:52
    2 126 06:59
    3 18 00:58
```

### №3.

### Входной файл:

```bash
    3
    07:00 18:00
    9
    08:00 1 ab1
    08:01 2 Ab1 2
```

### Вывод в консоль:
```bash
    07:00
    08:00 1 ab1
    08:01 2 Ab1 2
    Invalid event format.
```

### №4.

### Входной файл:

```bash
    2
    07:00 18:00
    10
    08:00 1 ab1
    08:00 1 ab2
    08:00 1 ab3
```

### Вывод в консоль:
```bash
    07:00
    08:00 1 ab1
    08:00 1 ab2
    08:00 1 ab3
    18:00 11 ab1
    18:00 11 ab2
    18:00 11 ab3
    18:00
    1 0 00:00
    2 0 00:00
```