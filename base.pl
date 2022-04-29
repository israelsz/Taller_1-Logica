%Representación de un videojuego registrado en la base de datos que puede
% permitir obtener una sugerencia de género de videojuegos para el usuario
%Formato: game(nombre_juego,genero, duración,antigüedad,dificultad,característica_extra)
% nombre_juego: String que indica el nombre de un videojuego, además puede ir
%               acompañado por un guión seguido de una categoría de speedrun
%               en el caso de que se quiere especificar un juego y su
%               categoría
% genero:       átomo que representa el genero/tipo de juego al cual corresponde el
%               el videojuego. Para la base la implementación se toman en cuenta los
%               generos representados por los átomos:
%               -puzzle
%               -plataforma
%               -sandbox
%               -metroidvania
% duracion:     átomos que representan la duracion de la run que posea word record en
%               speedrun para el juego en cuestion. Para la base de conocimiento se
%               toma en cuenta los tiempos representados por los átomos:
%               -dur_corta = duracion de la run menor a 30 minutos
%               -dur_media = duracion de la run entre 30 minutos y 90 minutos
%               -dur_larga = duracion de la run mayor a 90 minutos
% antiguedad:   atomos que representan la antiguedad del videojuego dependiendo su fecha
%               de lanzamiento. Para la base de conocimiento se consideran las antiguedades
%               -antiguo: juegos con fecha de lanzamiento anterior al 2000
%               -nuevo: juegos con fecha de lanzamiento posterior al 2000
% dificultad:   atomos que representan la dificultad del videojuego y de la run dependiendo
%               la cantidad de jugadores?? que activos intentando realizar la run. Los
%               atomos considerados para la base de conocimiento son:
%               -dif_media
%               -dif_facil
%               -dif_dificil
% caracteristica_extra: corresponde a alguna caracteristica propia del genero que puede
%               ayudar a determinar cual es la preferencia del usuario. Las
%               caracteristicas presentes en la base de conocimiento son
%               -etapas_distintas
%               -pensar
%               -mundo_abierto
%               -desbloquear_zonas
%

%Juegos de plataforma
game('Donkey Kong',plataforma,dur_media,antiguo,dif_media,etapas_distintas).
game('Crash Bandicoot',plataforma,dur_media,antiguo,dif_facil,etapas_distintas).
game('Cuphead',plataforma,dur_media,nuevo,dif_dificil,etapas_distintas).
game('Super Mario world',plataforma,dur_media,antiguo,dif_media,etapas_distintas).
game('Sonic The Hedgehog',plataforma,dur_corta,antiguo,dif_facil,etapas_distintas).

%Juegos de puzzle
game('Portal',puzzle,dur_corta,antiguo,dif_media,pensar).
game('Portal 2',puzzle,dur_media,nuevo,dif_media,pensar).
game('It takes two',puzzle,dur_larga,nuevo,dif_media,pensar).
game('Superliminal',puzzle,dur_corta,nuevo,dif_dificil,pensar).
game('Hitman:Codename 47',puzzle,dur_corta,antiguo,dif_facil,pensar).


%Juegos sandbox
game('Minecraft',sandbox,dur_media,antiguo,dif_facil,mundo_abierto).
game('Grand Theft Auto V',sandbox,dur_larga,nuevo,dif_facil,mundo_abierto).
game('Grand Theft Auto San Andreas',sandbox,dur_larga,antiguo,dif_media,mundo_abierto).
game('Elden Ring',sandbox,dur_corta,nuevo,dif_dificil,mundo_abierto).
game('Assasins Creed',sandbox,dur_larga,nuevo,dif_media,mundo_abierto).

%Juegos roguelike
game('Muck',roguelike,dur_corta,nuevo,dif_dificil,sin_historia).
game('Muck1',roguelike,dur_corta,nuevo,dif_dificil,sin_historia).
game('Muck2',roguelike,dur_corta,nuevo,dif_dificil,sin_historia).
game('Muck3',roguelike,dur_corta,nuevo,dif_dificil,sin_historia).
game('Muck4',roguelike,dur_corta,nuevo,dif_dificil,sin_historia).
game('Muck5',roguelike,dur_corta,nuevo,dif_dificil,sin_historia).
game('The Binding of Isaac Repentance',roguelike,dur_larga,nuevo,dif_media,sin_historia).
game('Hades',roguelike,dur_corta,nuevo,dif_media,sin_historia).
game('Enter the Gungeon',roguelike,dur_corta,nuevo,dif_facil,sin_historia).
game('Risk of Rain',roguelike,dur_corta,nuevo,dif_media,sin_historia).