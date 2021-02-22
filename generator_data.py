from dbModel import *
import random

name = ["carro1", "carro2", "carro3", "carro4", "carro5"]
# name = ["lancha", "bote"]

picture = [ 
           "http://eberesquivel.com/img/VTUIaBJ.jpg",
           "http://eberesquivel.com/img/HDHTs3j.jpg",
           "http://eberesquivel.com/img/HKbv7u7.jpg",
           "http://eberesquivel.com/img/quUVA5Tb.jpg",
           "http://eberesquivel.com/img/9RZL0j5b.jpg",
           "http://eberesquivel.com/img/keSmEdPb.jpg",
           "http://eberesquivel.com/img/buPaGzlb.jpg",
           "http://eberesquivel.com/img/5NzC1gvb.jpg",
           "http://eberesquivel.com/img/bote.jpg",
           "http://eberesquivel.com/img/lancha.jpg",
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
        insert_data = MapAutos(
            Name=name[index_name] + str(index),
            Picture=picture[index_pic],
            Color=color[index_color],
            Longitude=random.uniform( 18.0, 18.9),
            Latitude=random.uniform(18.0, 18.9),
        )
        db.session.add(insert_data)
    db.session.commit()
    print('Generator Data Done')

