import re

class RegExample:
    def __init__(self) -> None:
        pass


    @staticmethod
    def buscar(texto:str) -> list:
        #patron palabras que empiezan por vocal minúscula   
        patron = "\\b[aeiou][^\\s.,]*"
        result = re.findall(patron, texto)
        return result
    @staticmethod
    def validURL(url:str)-> bool:
        #patron para saber si una URL es valida
        patron = "^(https?|ftp):\/\/[^\s\/$.?#].[^\s]*$"
        result = re.match(patron, url)
        return result is not None
    

if __name__ == "__main__":
    text = ''' Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce feugiat efficitur sollicitudin. Mauris mollis efficitur ornare. Donec vulputate ligula ante, eu finibus purus maximus ut. Fusce vitae leo tincidunt, pharetra tellus quis, sollicitudin est. Phasellus et libero mi. Integer tincidunt est at magna molestie, sed vehicula ipsum dictum. Morbi ex nulla, interdum id ornare eu, hendrerit ac sapien. Etiam ac laoreet tellus. In interdum quam porta nisl euismod, id convallis metus pulvinar. Donec accumsan hendrerit turpis, in vehicula tortor mollis quis. Curabitur libero ipsum, molestie at blandit sed, viverra ut neque. Nunc in vestibulum risus, id scelerisque elit. Suspendisse in pharetra ipsum. Nulla non congue velit. Nullam pharetra, arcu quis posuere accumsan, urna libero sagittis diam, quis fringilla purus arcu quis dui.

In maximus volutpat mauris nec rutrum. Cras ultricies dui sed justo euismod vestibulum. Maecenas aliquet ultrices sapien, et venenatis justo eleifend a. Morbi quis posuere ipsum. Proin congue aliquam ante. Nam et quam auctor, facilisis tellus nec, pharetra magna. Ut mauris velit, mattis ut vehicula id, bibendum id mauris. Quisque dapibus turpis dui, iaculis interdum dolor ullamcorper sed. Curabitur scelerisque nulla et nulla condimentum tempus.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas mauris dui, mattis eget diam sit amet, vehicula sagittis ante. Nullam tempus sapien sed nunc iaculis, at lobortis diam fringilla. Duis imperdiet rutrum elementum. Nunc congue ligula neque, nec fermentum ligula tristique vel. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In volutpat augue vitae urna pharetra fringilla. Mauris urna odio, convallis vel purus eget, efficitur tempor tortor. Aliquam a interdum ligula. Sed tortor ligula, dapibus ut massa in, blandit lobortis ligula. Vivamus est nunc, vestibulum a tortor non, convallis aliquet nibh. Etiam cursus hendrerit purus vel elementum. Praesent sagittis, eros quis faucibus ullamcorper, est nunc maximus erat, sed feugiat lorem est in augue. Suspendisse mollis congue lorem, vel auctor dolor.

Fusce maximus auctor odio, sed pretium turpis egestas id. Nullam varius cursus porta. Curabitur posuere, urna non ultrices rhoncus, metus eros sagittis nibh, a consectetur magna lectus nec metus. Duis ipsum quam, tristique pretium ligula vel, sagittis suscipit nisl. Aliquam nec eros suscipit, convallis urna sit amet, tempus nulla. Nulla congue ipsum metus, a blandit justo faucibus id. Sed ac dignissim lectus. Etiam id mi dictum, consectetur ante sit amet, semper tellus. Curabitur efficitur nulla non turpis euismod ultrices. Nullam ullamcorper, tortor rhoncus viverra sodales, dui ante blandit nisi, vitae eleifend magna diam mollis eros. Fusce varius lobortis lacinia. Suspendisse potenti.

Nam velit diam, tempus non viverra sed, iaculis eget diam. Suspendisse rhoncus est leo, et sollicitudin mauris finibus at. Ut ipsum tellus, volutpat a ornare vitae, faucibus at metus. Curabitur nec ipsum tempus, eleifend magna id, convallis tortor. Duis massa nibh, venenatis eget nunc vel, tristique tempus massa. Curabitur sem quam, ornare porta odio in, feugiat auctor mauris. Mauris bibendum nunc sit amet dapibus tincidunt. Duis vel massa neque. Sed euismod neque sit amet ipsum malesuada vulputate. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada fringilla lectus ut accumsan. Etiam vitae velit finibus lorem pulvinar tincidunt. Sed ligula enim, semper a augue congue, auctor sagittis dolor. Nulla iaculis est ac velit ornare blandit. Phasellus ultrices fringilla magna, id feugiat libero laoreet id.
'''

    print(RegExample.buscar(text))