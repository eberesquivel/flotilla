from dbModel import *
import random

name = ["carro1", "carro2", "carro3", "carro4", "carro5"]
# name = ["lancha", "bote"]

picture = [ 
           "https://freepngimg.com/thumb/car/3-2-car-free-download-png.png",
           "https://freepngimg.com/thumb/car/7-2-car-free-png-image-thumb.png",
           "https://freepngimg.com/thumb/car/8-2-car-png-clipart-thumb.png",
           "https://freepngimg.com/thumb/car/60121-art-car-vector-bmw-m3-series-thumb.png",
           "https://freepngimg.com/thumb/car/60136-blue-i8-car-sports-m5-vr-bmw-thumb.png",
           "https://freepngimg.com/thumb/car/81496-fiat-car-toro-automobiles-motor-vehicle-thumb.png",
           "https://freepngimg.com/thumb/car/13-2-car-png-thumb.png",
           "https://freepngimg.com/thumb/car/5-2-car-png-pic-thumb.png",
           "https://freepngimg.com/thumb/boat/20773-3-transparent-boat-thumb.png",
           "https://freepngimg.com/thumb/boat/36647-3-boat-concept-thumb.png",
           ]

color = ["#E44040", "#EC21C7", "#8C4C80", "#A41FEC", "#B99ADA"
    , "#4E15E9", "#154EE9", "#4B9CF8", "#65BCD8", "#13EFE4"
    , "#13EFA2", "#13EF63", "#3E7753", "#8DBE1A", "#D6E6AE"
    , "#E8F669", "#949478", "#E4B92C", "#E98915", "#F2802E"]

if __name__ == '__main__':
    print('Start Generator Data......')
    for index in range(1, 11):
        index_name = random.randint(0, len(name) - 1)
        index_pic = random.randint(0, len(picture) - 1)
        index_color = random.randint(0, len(color) - 1)
        insert_data = MapPets(
            Name=name[index_name] + str(index),
            Picture=picture[index_pic],
            Color=color[index_color],
            Longitude=random.uniform( 18.0, 18.9),
            Latitude=random.uniform(18.0, 18.9),
        )
        db.session.add(insert_data)
    db.session.commit()
    print('Generator Data Done')

