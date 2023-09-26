# Conversor de Imagem
## Funcionalidade
Tem como objetivo converter uma imagem para o formato correto em que a impressora do fusion possa imprimir corretamente a imagem. Basicamente o processo é de tranformar a imagem do tipo RGB, RGBa... para o formato do tipo indexado, ou seja, cada pixel pode conter o valor 1 ou 0 (zero) para representar as cores preto ou branco. Também podemos converter as cores da imagem quando necessário, assim como poder definir o tamanho da imagem final.

Usabilidade do script de conversão:

```
python app.py -h
usage: Fusion Image Converter [-h] [-I IMAGE_IN] [-O IMAGE_OUTPUT] [-V] [-R]
                              [-S width height]

Convert a image to the proper format for using the fusion printer

optional arguments:
  -h, --help            show this help message and exit
  -I IMAGE_IN, --image-in IMAGE_IN
                        Image input path and name Default path: ./input.bmp
  -O IMAGE_OUTPUT, --image-output IMAGE_OUTPUT
                        Image ouput path and name Default path: ./ouput.bmp
  -V, --verbose
  -R, --invert-pixels   Invert image pixel colors
  -S width height, --size-output width height
                        Set image size
```

Pode-se utilizar o script sem utilizar nenhum parametro.

### Imagem de Entrada e de Saida
Caso seja necessario espcificar o nome da imagem pode-se utilizar da seguinte maneira:

```
python app.py --input-image teste.bmp
```

Ou pode ser utilizado assim:

```
python app.py -I teste.bmp
```

Podemos também especificar o nome da imagem resultante, por padrão, o nome da imagem convertida é output.bmp, para especificarmos o nome utilizamos da seguinte forma:

```
python app.py --input-image teste.bmp --image-ouput img-convertida.bmp
```
Ou:

```
python app.py -I teste.bmp -O img-convertida.bmp
```
### Processamentos adicionais de imagem
Ainda podemos utilizar mais duas operações:
  * Inverter as cores da imagem
  * Definir o tamanho da imagem processada

Para inverter as cores podemos utilizando o argumento de conversão da seguinte maneira:
```
python app.py --invert-pixels
```
Ou:
```
python app.py -R
```

Para definir o tamanho utilizamos o argumento de dimensão da seguinte maneira
```
python app.py --size-output 300 300
```
Ou:
```
python app.py -S 300 300
```


