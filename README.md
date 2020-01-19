# NEAT-AI
![Sample Run](https://github.com/Zafirmk/PropertyFinder/blob/master/SampleRun.gif)  

**Project duration**: 3 days  
**Text Editor**: Sublime Text (Community Edition)  
**Python Version**: Python 3.7  


## Description
The NEAT-AI works with a set population and a set number of generations. Where in each generation the best induviduals of a population are selected and bred. As the generations progress - only the best induviduals survive. Each induvidual in the population has a neural network associated with it which manuvers it through the game.


## How it works
* Each genome *player* has a neural network and a fitness score assigned to it.

* Fitness is the *score* associated with the genome. The better the genome's performance, the better it's fitness.

* After each passing generation genomes with the highest fitness are selected and bred - this process is repeated for n generations until a superior genome is created.

* The neural network associated with each genome is as follows:

* [Neural Network](placeholder)

* Where inputs x1, x2, x3, x4, x5 are the positions of the four asteroids and the position of the genome.

* Through the ConfigFile.txt all parameters can be edited.



### Prerequisites
Things you need to install before running:
*  [Python](https://www.python.org/)
*  [NEAT](https://neat-python.readthedocs.io/en/latest/)

#### Additional Notes
*  Check [AsteroidAvoider](https://github.com/Zafirmk/AsteroidAvoider) to see how the game was created. 
