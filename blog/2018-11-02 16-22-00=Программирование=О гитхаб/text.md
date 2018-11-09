Предварительный текст для новой статьи: "О гитхаб". Из раздела "Программирование". Должно все работать 6.

Меркдаун или как там его, очень легко позволяет сделать текст **толстым**, также легко позволяет сделать текст *италиком*. Можно очень легко замутить [ссылку на Google!](http://google.com)

```
Меркдаун или как там его, очень легко позволяет сделать текст **толстым**, также легко позволяет сделать текст *италиком*. Можно очень легко замутить [ссылку на Google!](http://google.com)
```

# Шапка тегом Ха1
## Шапка тегом Ха2
###### Шапка тегом Ха6

```
# Шапка тегом Ха1
## Шапка тегом Ха2
###### Шапка тегом Ха6
```

Если охота списка номерками:
1. Одноко
2. Двоко
3. Троко

```
Если охота списка номерками:
1. Одноко
2. Двоко
3. Троко
```

Можно также хотеть и списка не номерками:
* Ненумерованый пункт;
* Ненумерованый пункт;

```
Можно также хотеть и списка не номерками:
* Ненумерованый пункт;
* Ненумерованый пункт;
```

Списки со вложенностью через тире:
- Dashes work just as well
- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this

```
Списки со вложенностью через тире:
- Dashes work just as well
- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this
```

Картинки вставляются как-то так:
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

```
Картинки вставляются как-то так:
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
```

Еще можно мутить что-то похожее на сноски:
> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway

```
Еще можно мутить что-то похожее на сноски:
> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway
```

Код думаю вставлять желательно вот так:
```
if (isAwesome){
  return true
}
```
Или можно вставлять указав что это за язык:
```Python
def file_to_wb(file_name):
    try:
        return openpyxl.load_workbook(filename=file_name)
    except:
        logger.critical('Ошибка открытия файла: %s' % (file_name))
        exit(0)
```