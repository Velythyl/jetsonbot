import argparse
import random
import signal
import subprocess
import sys
from time import sleep

# TODO split out the output of the dockers into separate log files, i guess?

old_print = print
def print(string):
    old_print(string, file=sys.stderr)


def list_of_str(string):
    string = string.replace("[").replace("]")
    listed = string.split(",")
    return map(float, listed)


def signal_handler(sig, frame):
    handle_exit()

def cleanup_docker_name(string):
    return string.split(" ")[-1]

def handle_exit():
    for docker in genned_names:
        try:
            print(subprocess.check_output(("docker stop "+docker).split(" "),
                                          universal_newlines=True))
        except Exception as e:
            print(e)
            print("Trying to kill instead")
            try:
                print(subprocess.check_output(("docker kill "+docker).split(" "),
                                              universal_newlines=True))
            except Exception as e:
                print(e)
                print(f"You will have to kill '{docker}' yourself")
                
    for pipe in pipes:
        pipe.close()
    exit()

genned_names = []
def gen_name():
    global genned_names
    def do_it():
        adj = ['abandoned', 'able', 'absolute', 'adorable', 'adventurous', 'academic', 'acceptable', 'acclaimed', 'accomplished', 'accurate', 'aching', 'acidic', 'acrobatic', 'active', 'actual', 'adept', 'admirable', 'admired', 'adolescent', 'adorable', 'adored', 'advanced', 'afraid', 'affectionate', 'aged', 'aggravating', 'aggressive', 'agile', 'agitated', 'agonizing', 'agreeable', 'ajar', 'alarmed', 'alarming', 'alert', 'alienated', 'alive', 'all', 'altruistic', 'amazing', 'ambitious', 'ample', 'amused', 'amusing', 'anchored', 'ancient', 'angelic', 'angry', 'anguished', 'animated', 'annual', 'another', 'antique', 'anxious', 'any', 'apprehensive', 'appropriate', 'apt', 'arctic', 'arid', 'aromatic', 'artistic', 'ashamed', 'assured', 'astonishing', 'athletic', 'attached', 'attentive', 'attractive', 'austere', 'authentic', 'authorized', 'automatic', 'avaricious', 'average', 'aware', 'awesome', 'awful', 'awkward', 'babyish', 'bad', 'back', 'baggy', 'bare', 'barren', 'basic', 'beautiful', 'belated', 'beloved', 'beneficial', 'better', 'best', 'bewitched', 'big', 'big-hearted', 'biodegradable', 'bite-sized', 'bitter', 'black', 'black-and-white', 'bland', 'blank', 'blaring', 'bleak', 'blind', 'blissful', 'blond', 'blue', 'blushing', 'bogus', 'boiling', 'bold', 'bony', 'boring', 'bossy', 'both', 'bouncy', 'bountiful', 'bowed', 'brave', 'breakable', 'brief', 'bright', 'brilliant', 'brisk', 'broken', 'bronze', 'brown', 'bruised', 'bubbly', 'bulky', 'bumpy', 'buoyant', 'burdensome', 'burly', 'bustling', 'busy', 'buttery', 'buzzing', 'calculating', 'calm', 'candid', 'canine', 'capital', 'carefree', 'careful', 'careless', 'caring', 'cautious', 'cavernous', 'celebrated', 'charming', 'cheap', 'cheerful', 'cheery', 'chief', 'chilly', 'chubby', 'circular', 'classic', 'clean', 'clear', 'clear-cut', 'clever', 'close', 'closed', 'cloudy', 'clueless', 'clumsy', 'cluttered', 'coarse', 'cold', 'colorful', 'colorless', 'colossal', 'comfortable', 'common', 'compassionate', 'competent', 'complete', 'complex', 'complicated', 'composed', 'concerned', 'concrete', 'confused', 'conscious', 'considerate', 'constant', 'content', 'conventional', 'cooked', 'cool', 'cooperative', 'coordinated', 'corny', 'corrupt', 'costly', 'courageous', 'courteous', 'crafty', 'crazy', 'creamy', 'creative', 'creepy', 'criminal', 'crisp', 'critical', 'crooked', 'crowded', 'cruel', 'crushing', 'cuddly', 'cultivated', 'cultured', 'cumbersome', 'curly', 'curvy', 'cute', 'cylindrical', 'damaged', 'damp', 'dangerous', 'dapper', 'daring', 'darling', 'dark', 'dazzling', 'dead', 'deadly', 'deafening', 'dear', 'dearest', 'decent', 'decimal', 'decisive', 'deep', 'defenseless', 'defensive', 'defiant', 'deficient', 'definite', 'definitive', 'delayed', 'delectable', 'delicious', 'delightful', 'delirious', 'demanding', 'dense', 'dental', 'dependable', 'dependent', 'descriptive', 'deserted', 'detailed', 'determined', 'devoted', 'different', 'difficult', 'digital', 'diligent', 'dim', 'dimpled', 'dimwitted', 'direct', 'disastrous', 'discrete', 'disfigured', 'disgusting', 'disloyal', 'dismal', 'distant', 'downright', 'dreary', 'dirty', 'disguised', 'dishonest', 'dismal', 'distant', 'distinct', 'distorted', 'dizzy', 'dopey', 'doting', 'double', 'downright', 'drab', 'drafty', 'dramatic', 'dreary', 'droopy', 'dry', 'dual', 'dull', 'dutiful', 'each', 'eager', 'earnest', 'early', 'easy', 'easy-going', 'ecstatic', 'edible', 'educated', 'elaborate', 'elastic', 'elated', 'elderly', 'electric', 'elegant', 'elementary', 'elliptical', 'embarrassed', 'embellished', 'eminent', 'emotional', 'empty', 'enchanted', 'enchanting', 'energetic', 'enlightened', 'enormous', 'enraged', 'entire', 'envious', 'equal', 'equatorial', 'essential', 'esteemed', 'ethical', 'euphoric', 'even', 'evergreen', 'everlasting', 'every', 'evil', 'exalted', 'excellent', 'exemplary', 'exhausted', 'excitable', 'excited', 'exciting', 'exotic', 'expensive', 'experienced', 'expert', 'extraneous', 'extroverted', 'extra-large', 'extra-small', 'fabulous', 'failing', 'faint', 'fair', 'faithful', 'fake', 'false', 'familiar', 'famous', 'fancy', 'fantastic', 'far', 'faraway', 'far-flung', 'far-off', 'fast', 'fat', 'fatal', 'fatherly', 'favorable', 'favorite', 'fearful', 'fearless', 'feisty', 'feline', 'female', 'feminine', 'few', 'fickle', 'filthy', 'fine', 'finished', 'firm', 'first', 'firsthand', 'fitting', 'fixed', 'flaky', 'flamboyant', 'flashy', 'flat', 'flawed', 'flawless', 'flickering', 'flimsy', 'flippant', 'flowery', 'fluffy', 'fluid', 'flustered', 'focused', 'fond', 'foolhardy', 'foolish', 'forceful', 'forked', 'formal', 'forsaken', 'forthright', 'fortunate', 'fragrant', 'frail', 'frank', 'frayed', 'free', 'french', 'fresh', 'frequent', 'friendly', 'frightened', 'frightening', 'frigid', 'frilly', 'frizzy', 'frivolous', 'front', 'frosty', 'frozen', 'frugal', 'fruitful', 'full', 'fumbling', 'functional', 'funny', 'fussy', 'fuzzy', 'gargantuan', 'gaseous', 'general', 'generous', 'gentle', 'genuine', 'giant', 'giddy', 'gigantic']
        animals = ['canidae', 'felidae', 'cat', 'cattle', 'dog', 'donkey', 'goat', 'pig', 'horse', 'pig', 'rabbit', 'varieties', 'strains', 'breeds', 'breeds', 'breeds', 'breeds', 'breeds', 'breeds', 'breeds', 'aardvark', 'aardwolf', 'buffalo', 'elephant', 'leopard', 'albatross', 'alligator', 'alpaca', '(bison)', 'robin', 'amphibian', 'list', 'anaconda', 'angelfish', 'anglerfish', 'ant', 'anteater', 'antelope', 'antlion', 'ape', 'aphid', 'leopard', 'fox', 'wolf', 'armadillo', 'crab', 'asp', '(donkey)', 'baboon', 'badger', 'eagle', 'bandicoot', 'barnacle', 'barracuda', 'basilisk', 'bass', 'bat', 'whale', 'bear', 'list', 'beaver', 'bedbug', 'bee', 'beetle', 'bird', 'list', 'bison', 'blackbird', 'panther', 'spider', 'bird', 'jay', 'whale', 'boa', 'boar', 'bobcat', 'bobolink', 'bonobo', 'booby', 'jellyfish', 'bovid', 'african', '(bison)', 'bug', 'butterfly', 'buzzard', 'camel', 'canid', 'buffalo', 'capybara', 'cardinal', 'caribou', 'carp', 'cat', 'list', 'catshark', 'caterpillar', 'catfish', 'cattle', 'list', 'centipede', 'cephalopod', 'chameleon', 'cheetah', 'chickadee', 'chicken', 'list', 'chimpanzee', 'chinchilla', 'chipmunk', 'clam', 'clownfish', 'cobra', 'cockroach', 'cod', 'condor', 'constrictor', 'coral', 'cougar', 'cow', 'coyote', 'crab', 'crane', 'fly', 'crawdad', 'crayfish', 'cricket', 'crocodile', 'crow', 'cuckoo', 'cicada', 'damselfly', 'deer', 'dingo', 'dinosaur', 'list', 'dog', 'list', 'dolphin', 'donkey', 'list', 'dormouse', 'dove', 'dragonfly', 'dragon', 'duck', 'list', 'beetle', 'eagle', 'earthworm', 'earwig', 'echidna', 'eel', 'egret', 'elephant', 'seal', 'elk', 'emu', 'pointer', 'ermine', 'falcon', 'ferret', 'finch', 'firefly', 'fish', 'flamingo', 'flea', 'fly', 'flyingfish', 'fowl', 'fox', 'frog', 'bat', 'gamefowl', 'list', 'galliform', 'list', 'gazelle', 'gecko', 'gerbil', 'panda', 'squid', 'gibbon', 'monster', 'giraffe', 'goat', 'list', 'goldfish', 'goose', 'list', 'gopher', 'gorilla', 'grasshopper', 'heron', 'shark', 'bear', 'shark', 'sloth', 'grouse', 'guan', 'list', 'guanaco', 'guineafowl', 'list', 'pig', 'list', 'gull', 'guppy', 'haddock', 'halibut', 'shark', 'hamster', 'hare', 'harrier', 'hawk', 'hedgehog', 'crab', 'heron', 'herring', 'hippopotamus', 'hookworm', 'hornet', 'horse', 'list', 'hoverfly', 'hummingbird', 'whale', 'hyena', 'iguana', 'impala', 'jellyfish', 'jackal', 'jaguar', 'jay', 'jellyfish', 'junglefowl', 'kangaroo', 'mouse', 'rat', 'kingfisher', 'kite', 'kiwi', 'koala', 'koi', 'dragon', 'krill', 'ladybug', 'lamprey', 'landfowl', 'snail', 'lark', 'leech', 'lemming', 'lemur', 'leopard', 'leopon', 'limpet', 'lion', 'lizard', 'llama', 'lobster', 'locust', 'loon', 'louse', 'lungfish', 'lynx', 'macaw', 'mackerel', 'magpie', 'mammal', 'manatee', 'mandrill', 'ray', 'marlin', 'marmoset', 'marmot', 'marsupial', 'marten', 'mastodon', 'meadowlark', 'meerkat', 'mink', 'minnow', 'mite', 'mockingbird', 'mole', 'mollusk', 'mongoose', 'lizard', 'monkey', 'moose', 'mosquito', 'moth', 'goat', 'mouse', 'mule', 'muskox', 'narwhal', 'newt', 'quail', 'nightingale', 'ocelot', 'octopus', 'quail', 'opossum', 'orangutan', 'orca', 'ostrich', 'otter', 'owl', 'ox', 'panda', 'panther', 'hybrid', 'parakeet', 'parrot', 'parrotfish', 'partridge', 'peacock', 'peafowl', 'pelican', 'penguin', 'perch', 'falcon', 'pheasant', 'pig', 'pigeon', 'list', 'pike', 'whale', 'pinniped', 'piranha', 'planarian', 'platypus', 'bear', 'pony', 'porcupine', 'porpoise', 'war', 'possum', 'dog', 'prawn', 'mantis', 'primate', 'ptarmigan', 'puffin', 'puma', 'python', 'quail', 'quelea', 'quokka', 'rabbit', 'list', 'raccoon', 'trout', 'rat', 'rattlesnake', 'raven', '(batoidea)', '(rajiformes)', 'panda', 'reindeer', 'reptile', 'rhinoceros', 'whale', 'roadrunner', 'rodent', 'rook', 'rooster', 'roundworm', 'cat', 'sailfish', 'salamander', 'salmon', 'sawfish', 'insect', 'scallop', 'scorpion', 'seahorse', 'lion', 'slug', 'snail', 'shark', 'list', 'sheep', 'list', 'shrew', 'shrimp', 'silkworm', 'silverfish', 'skink', 'skunk', 'sloth', 'slug', 'smelt', 'snail', 'snake', 'list', 'snipe', 'leopard', 'salmon', 'sole', 'sparrow', 'whale', 'spider', 'monkey', 'spoonbill', 'squid', 'squirrel', 'starfish', 'mole', 'trout', 'stingray', 'stoat', 'stork', 'sturgeon', 'glider', 'swallow', 'swan', 'swift', 'swordfish', 'swordtail', 'tahr', 'takin', 'tapir', 'tarantula', 'tarsier', 'devil', 'termite', 'tern', 'thrush', 'tick', 'tiger', 'shark', 'tiglon', 'toad', 'tortoise', 'toucan', 'spider', 'frog', 'trout', 'tuna', 'turkey', 'list', 'turtle', 'tyrannosaurus', 'urial', 'bat', 'squid', 'vicuna', 'viper', 'vole', 'vulture', 'wallaby', 'walrus', 'wasp', 'warbler', 'boa', 'buffalo', 'weasel', 'whale', 'whippet', 'whitefish', 'crane', 'wildcat', 'wildebeest', 'wildfowl', 'wolf', 'wolverine', 'wombat', 'woodpecker', 'worm', 'wren', 'xerinae', 'fish', 'yak', 'perch', 'zebra', 'finch', 'neurons', 'size', 'pests', 'animals', 'alpaca', 'cattle', 'cat', 'cattle', 'chicken', 'dog', 'camel', 'canary', 'camel', 'duck', 'goat', 'goose', 'guineafowl', 'hedgehog', 'pig', 'pigeon', 'rabbit', 'silkmoth', 'fox', 'turkey', 'donkey', 'mouse', 'rat', 'rat', 'ferret', 'gayal', 'goldfish', 'pig', 'guppy', 'horse', 'koi', 'llama', 'dove', 'sheep', 'fish', 'finch', 'yak', 'buffalo']
        return random.choice(adj)+"-"+random.choice(animals)


    name = do_it()
    while name in genned_names:
        name = do_it()

    genned_names.append(name)
    return name




signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dockers", default=[], type=list_of_str)
parser = parser.parse_args()

dockers_to_run = [
                     "duckietown/dt-duckiebot-interface:daffy-arm32v7",
                     "duckietown/dt-car-interface:daffy-arm32v7",
                     "--gpus all duckietown/dt-core:daffy-arm32v7"
                 ] + parser.dockers


print(f"Dockers to run, sequentially: {', '.join(map(cleanup_docker_name, dockers_to_run))}")

processes = []
pipes = []
for docker in dockers_to_run:
    command = f"docker run --net=host -v /home/jetsonbot/data:/data --privileged --device=/dev/vchiq:/dev/vchiq --name {gen_name()} {docker}"

    pipes.append(open(cleanup_docker_name(docker).split("/")[-1]+".log", "w"))

    processes.append(subprocess.Popen(command.split(" "), universal_newlines=True, stdout=pipes[-1], stderr=pipes[-1]))

    print(f"Started '{cleanup_docker_name(docker)}'.")

    sleep(60)   # timing issues https://answers.ros.org/question/310848/run_id-on-parameter-server-does-not-match-declared-run_id/


def fake_func():
    while True:
        for i, process in enumerate(processes):
            if process.poll() is not None:
                print(
                    f"DOCKER LAUNCHER REPORT: process '{cleanup_docker_name(dockers_to_run[i])}' has died. \nExiting now.",
                    )
                return
        sleep(10)


fake_func()
handle_exit()
