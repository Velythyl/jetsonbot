import argparse
import random
import signal
import subprocess
import sys
from time import sleep


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
            print(subprocess.check_output(("docker stop " + cleanup_docker_name(docker)).split(" "),
                                          universal_newlines=True))
        except Exception as e:
            print(e)
            print("Trying to kill instead")
            try:
                print(subprocess.check_output(("docker kill " + cleanup_docker_name(docker)).split(" "),
                                              universal_newlines=True))
            except Exception as e:
                print(e)
                print(f"You will have to kill '{cleanup_docker_name(docker)}' yourself")
    exit()

genned_names = []
def gen_name():
    global genned_names
    def do_it():
        adj = ['abandoned', 'able', 'absolute', 'adorable', 'adventurous', 'academic', 'acceptable', 'acclaimed', 'accomplished', 'accurate', 'aching', 'acidic', 'acrobatic', 'active', 'actual', 'adept', 'admirable', 'admired', 'adolescent', 'adorable', 'adored', 'advanced', 'afraid', 'affectionate', 'aged', 'aggravating', 'aggressive', 'agile', 'agitated', 'agonizing', 'agreeable', 'ajar', 'alarmed', 'alarming', 'alert', 'alienated', 'alive', 'all', 'altruistic', 'amazing', 'ambitious', 'ample', 'amused', 'amusing', 'anchored', 'ancient', 'angelic', 'angry', 'anguished', 'animated', 'annual', 'another', 'antique', 'anxious', 'any', 'apprehensive', 'appropriate', 'apt', 'arctic', 'arid', 'aromatic', 'artistic', 'ashamed', 'assured', 'astonishing', 'athletic', 'attached', 'attentive', 'attractive', 'austere', 'authentic', 'authorized', 'automatic', 'avaricious', 'average', 'aware', 'awesome', 'awful', 'awkward', 'babyish', 'bad', 'back', 'baggy', 'bare', 'barren', 'basic', 'beautiful', 'belated', 'beloved', 'beneficial', 'better', 'best', 'bewitched', 'big', 'big-hearted', 'biodegradable', 'bite-sized', 'bitter', 'black', 'black-and-white', 'bland', 'blank', 'blaring', 'bleak', 'blind', 'blissful', 'blond', 'blue', 'blushing', 'bogus', 'boiling', 'bold', 'bony', 'boring', 'bossy', 'both', 'bouncy', 'bountiful', 'bowed', 'brave', 'breakable', 'brief', 'bright', 'brilliant', 'brisk', 'broken', 'bronze', 'brown', 'bruised', 'bubbly', 'bulky', 'bumpy', 'buoyant', 'burdensome', 'burly', 'bustling', 'busy', 'buttery', 'buzzing', 'calculating', 'calm', 'candid', 'canine', 'capital', 'carefree', 'careful', 'careless', 'caring', 'cautious', 'cavernous', 'celebrated', 'charming', 'cheap', 'cheerful', 'cheery', 'chief', 'chilly', 'chubby', 'circular', 'classic', 'clean', 'clear', 'clear-cut', 'clever', 'close', 'closed', 'cloudy', 'clueless', 'clumsy', 'cluttered', 'coarse', 'cold', 'colorful', 'colorless', 'colossal', 'comfortable', 'common', 'compassionate', 'competent', 'complete', 'complex', 'complicated', 'composed', 'concerned', 'concrete', 'confused', 'conscious', 'considerate', 'constant', 'content', 'conventional', 'cooked', 'cool', 'cooperative', 'coordinated', 'corny', 'corrupt', 'costly', 'courageous', 'courteous', 'crafty', 'crazy', 'creamy', 'creative', 'creepy', 'criminal', 'crisp', 'critical', 'crooked', 'crowded', 'cruel', 'crushing', 'cuddly', 'cultivated', 'cultured', 'cumbersome', 'curly', 'curvy', 'cute', 'cylindrical', 'damaged', 'damp', 'dangerous', 'dapper', 'daring', 'darling', 'dark', 'dazzling', 'dead', 'deadly', 'deafening', 'dear', 'dearest', 'decent', 'decimal', 'decisive', 'deep', 'defenseless', 'defensive', 'defiant', 'deficient', 'definite', 'definitive', 'delayed', 'delectable', 'delicious', 'delightful', 'delirious', 'demanding', 'dense', 'dental', 'dependable', 'dependent', 'descriptive', 'deserted', 'detailed', 'determined', 'devoted', 'different', 'difficult', 'digital', 'diligent', 'dim', 'dimpled', 'dimwitted', 'direct', 'disastrous', 'discrete', 'disfigured', 'disgusting', 'disloyal', 'dismal', 'distant', 'downright', 'dreary', 'dirty', 'disguised', 'dishonest', 'dismal', 'distant', 'distinct', 'distorted', 'dizzy', 'dopey', 'doting', 'double', 'downright', 'drab', 'drafty', 'dramatic', 'dreary', 'droopy', 'dry', 'dual', 'dull', 'dutiful', 'each', 'eager', 'earnest', 'early', 'easy', 'easy-going', 'ecstatic', 'edible', 'educated', 'elaborate', 'elastic', 'elated', 'elderly', 'electric', 'elegant', 'elementary', 'elliptical', 'embarrassed', 'embellished', 'eminent', 'emotional', 'empty', 'enchanted', 'enchanting', 'energetic', 'enlightened', 'enormous', 'enraged', 'entire', 'envious', 'equal', 'equatorial', 'essential', 'esteemed', 'ethical', 'euphoric', 'even', 'evergreen', 'everlasting', 'every', 'evil', 'exalted', 'excellent', 'exemplary', 'exhausted', 'excitable', 'excited', 'exciting', 'exotic', 'expensive', 'experienced', 'expert', 'extraneous', 'extroverted', 'extra-large', 'extra-small', 'fabulous', 'failing', 'faint', 'fair', 'faithful', 'fake', 'false', 'familiar', 'famous', 'fancy', 'fantastic', 'far', 'faraway', 'far-flung', 'far-off', 'fast', 'fat', 'fatal', 'fatherly', 'favorable', 'favorite', 'fearful', 'fearless', 'feisty', 'feline', 'female', 'feminine', 'few', 'fickle', 'filthy', 'fine', 'finished', 'firm', 'first', 'firsthand', 'fitting', 'fixed', 'flaky', 'flamboyant', 'flashy', 'flat', 'flawed', 'flawless', 'flickering', 'flimsy', 'flippant', 'flowery', 'fluffy', 'fluid', 'flustered', 'focused', 'fond', 'foolhardy', 'foolish', 'forceful', 'forked', 'formal', 'forsaken', 'forthright', 'fortunate', 'fragrant', 'frail', 'frank', 'frayed', 'free', 'french', 'fresh', 'frequent', 'friendly', 'frightened', 'frightening', 'frigid', 'frilly', 'frizzy', 'frivolous', 'front', 'frosty', 'frozen', 'frugal', 'fruitful', 'full', 'fumbling', 'functional', 'funny', 'fussy', 'fuzzy', 'gargantuan', 'gaseous', 'general', 'generous', 'gentle', 'genuine', 'giant', 'giddy', 'gigantic']
        animals = ['aardvark', 'abyssinian', 'adelie penguin', 'affenpinscher', 'afghan hound', 'african bush elephant', 'african civet', 'african clawed frog', 'african forest elephant', 'african palm civet', 'african penguin', 'african tree toad', 'african wild dog', 'ainu dog', 'airedale terrier', 'akbash', 'akita', 'alaskan malamute', 'albatross', 'aldabra giant tortoise', 'alligator', 'alpine dachsbracke', 'american bulldog', 'american cocker spaniel', 'american coonhound', 'american eskimo dog', 'american foxhound', 'american pit bull terrier', 'american staffordshire terrier', 'american water spaniel', 'anatolian shepherd dog', 'angelfish', 'ant', 'anteater', 'antelope', 'appenzeller dog', 'arctic fox', 'arctic hare', 'arctic wolf', 'armadillo', 'asian elephant', 'asian giant hornet', 'asian palm civet', 'asiatic black bear', 'australian cattle dog', 'australian kelpie dog', 'australian mist', 'australian shepherd', 'australian terrier', 'avocet', 'axolotl', 'aye aye', 'baboon', 'bactrian camel', 'badger', 'balinese', 'banded palm civet', 'bandicoot', 'barb', 'barn owl', 'barnacle', 'barracuda', 'basenji dog', 'basking shark', 'basset hound', 'bat', 'bavarian mountain hound', 'beagle', 'bear', 'bearded collie', 'bearded dragon', 'beaver', 'bedlington terrier', 'beetle', 'bengal tiger', 'bernese mountain dog', 'bichon frise', 'binturong', 'bird', 'birds of paradise', 'birman', 'bison', 'black bear', 'black rhinoceros', 'black russian terrier', 'black widow spider', 'bloodhound', 'blue lacy dog', 'blue whale', 'bluetick coonhound', 'bobcat', 'bolognese dog', 'bombay', 'bongo', 'bonobo', 'booby', 'border collie', 'border terrier', 'bornean orang-utan', 'borneo elephant', 'boston terrier', 'bottle nosed dolphin', 'boxer dog', 'boykin spaniel', 'brazilian terrier', 'brown bear', 'budgerigar', 'buffalo', 'bull mastiff', 'bull shark', 'bull terrier', 'bulldog', 'bullfrog', 'bumble bee', 'burmese', 'burrowing frog', 'butterfly', 'butterfly fish', 'caiman', 'caiman lizard', 'cairn terrier', 'camel', 'canaan dog', 'capybara', 'caracal', 'carolina dog', 'cassowary', 'cat', 'caterpillar', 'catfish', 'cavalier king charles spaniel', 'centipede', 'cesky fousek', 'chameleon', 'chamois', 'cheetah', 'chesapeake bay retriever', 'chicken', 'chihuahua', 'chimpanzee', 'chinchilla', 'chinese crested dog', 'chinook', 'chinstrap penguin', 'chipmunk', 'chow chow', 'cichlid', 'clouded leopard', 'clown fish', 'clumber spaniel', 'coati', 'cockroach', 'collared peccary', 'collie', 'common buzzard', 'common frog', 'common loon', 'common toad', 'coral', 'cottontop tamarin', 'cougar', 'cow', 'coyote', 'crab', 'crab-eating macaque', 'crane', 'crested penguin', 'crocodile', 'cross river gorilla', 'curly coated retriever', 'cuscus', 'cuttlefish', 'dachshund', 'dalmatian', "darwin's frog", 'deer', 'desert tortoise', 'deutsche bracke', 'dhole', 'dingo', 'discus', 'doberman pinscher', 'dodo', 'dog', 'dogo argentino', 'dogue de bordeaux', 'dolphin', 'donkey', 'dormouse', 'dragonfly', 'drever', 'duck', 'dugong', 'dunker', 'dusky dolphin', 'dwarf crocodile', 'eagle', 'earwig', 'eastern gorilla', 'eastern lowland gorilla', 'echidna', 'edible frog', 'egyptian mau', 'electric eel', 'elephant', 'elephant seal', 'elephant shrew', 'emperor penguin', 'emperor tamarin', 'emu', 'english cocker spaniel', 'english shepherd', 'english springer spaniel', 'entlebucher mountain dog', 'epagneul pont audemer', 'eskimo dog', 'estrela mountain dog', 'falcon', 'fennec fox', 'ferret', 'field spaniel', 'fin whale', 'finnish spitz', 'fire-bellied toad', 'fish', 'fishing cat', 'flamingo', 'flat coat retriever', 'flounder', 'fly', 'flying squirrel', 'fossa', 'fox', 'fox terrier', 'french bulldog', 'frigatebird', 'frilled lizard', 'frog', 'fur seal', 'galapagos penguin', 'galapagos tortoise', 'gar', 'gecko', 'gentoo penguin', 'geoffroys tamarin', 'gerbil', 'german pinscher', 'german shepherd', 'gharial', 'giant african land snail', 'giant clam', 'giant panda bear', 'giant schnauzer', 'gibbon', 'gila monster', 'giraffe', 'glass lizard', 'glow worm', 'goat', 'golden lion tamarin', 'golden oriole', 'golden retriever', 'goose', 'gopher', 'gorilla', 'grasshopper', 'great dane', 'great white shark', 'greater swiss mountain dog', 'green bee-eater', 'greenland dog', 'grey mouse lemur', 'grey reef shark', 'grey seal', 'greyhound', 'grizzly bear', 'grouse', 'guinea fowl', 'guinea pig', 'guppy', 'hammerhead shark', 'hamster', 'hare', 'harrier', 'havanese', 'hedgehog', 'hercules beetle', 'hermit crab', 'heron', 'highland cattle', 'himalayan', 'hippopotamus', 'honey bee', 'horn shark', 'horned frog', 'horse', 'horseshoe crab', 'howler monkey', 'human', 'humboldt penguin', 'hummingbird', 'humpback whale', 'hyena', 'ibis', 'ibizan hound', 'iguana', 'impala', 'indian elephant', 'indian palm squirrel', 'indian rhinoceros', 'indian star tortoise', 'indochinese tiger', 'indri', 'insect', 'irish setter', 'irish wolfhound', 'jack russel', 'jackal', 'jaguar', 'japanese chin', 'japanese macaque', 'javan rhinoceros', 'javanese', 'jellyfish', 'kakapo', 'kangaroo', 'keel billed toucan', 'killer whale', 'king crab', 'king penguin', 'kingfisher', 'kiwi', 'koala', 'komodo dragon', 'kudu', 'labradoodle', 'labrador retriever', 'ladybird', 'leaf-tailed gecko', 'lemming', 'lemur', 'leopard', 'leopard cat', 'leopard seal', 'leopard tortoise', 'liger', 'lion', 'lionfish', 'little penguin', 'lizard', 'llama', 'lobster', 'long-eared owl', 'lynx', 'macaroni penguin', 'macaw', 'magellanic penguin', 'magpie', 'maine coon', 'malayan civet', 'malayan tiger', 'maltese', 'manatee', 'mandrill', 'manta ray', 'marine toad', 'markhor', 'marsh frog', 'masked palm civet', 'mastiff', 'mayfly', 'meerkat', 'millipede', 'minke whale', 'mole', 'molly', 'mongoose', 'mongrel', 'monitor lizard', 'monkey', 'monte iberia eleuth', 'moorhen', 'moose', 'moray eel', 'moth', 'mountain gorilla', 'mountain lion', 'mouse', 'mule', 'neanderthal', 'neapolitan mastiff', 'newfoundland', 'newt', 'nightingale', 'norfolk terrier', 'norwegian forest', 'numbat', 'nurse shark', 'ocelot', 'octopus', 'okapi', 'old english sheepdog', 'olm', 'opossum', 'orang-utan', 'ostrich', 'otter', 'oyster', 'pademelon', 'panther', 'parrot', 'patas monkey', 'peacock', 'pekingese', 'pelican', 'penguin', 'persian', 'pheasant', 'pied tamarin', 'pig', 'pika', 'pike', 'pink fairy armadillo', 'piranha', 'platypus', 'pointer', 'poison dart frog', 'polar bear', 'pond skater', 'poodle', 'pool frog', 'porcupine', 'possum', 'prawn', 'proboscis monkey', 'puffer fish', 'puffin', 'pug', 'puma', 'purple emperor', 'puss moth', 'pygmy hippopotamus', 'pygmy marmoset', 'quail', 'quetzal', 'quokka', 'quoll', 'rabbit', 'raccoon', 'raccoon dog', 'radiated tortoise', 'ragdoll', 'rat', 'rattlesnake', 'red knee tarantula', 'red panda', 'red wolf', 'red-handed tamarin', 'reindeer', 'rhinoceros', 'river dolphin', 'river turtle', 'robin', 'rock hyrax', 'rockhopper penguin', 'roseate spoonbill', 'rottweiler', 'royal penguin', 'russian blue', 'sabre-toothed tiger', 'saint bernard', 'salamander', 'sand lizard', 'saola', 'scorpion', 'scorpion fish', 'sea dragon', 'sea lion', 'sea otter', 'sea slug', 'sea squirt', 'sea turtle', 'sea urchin', 'seahorse', 'seal', 'serval', 'sheep', 'shih tzu', 'shrimp', 'siamese', 'siamese fighting fish', 'siberian', 'siberian husky', 'siberian tiger', 'silver dollar', 'skunk', 'sloth', 'slow worm', 'snail', 'snake', 'snapping turtle', 'snowshoe', 'snowy owl', 'somali', 'south china tiger', 'spadefoot toad', 'sparrow', 'spectacled bear', 'sperm whale', 'spider monkey', 'spiny dogfish', 'sponge', 'squid', 'squirrel', 'squirrel monkey', 'sri lankan elephant', 'staffordshire bull terrier', 'stag beetle', 'starfish', 'stellers sea cow', 'stick insect', 'stingray', 'stoat', 'striped rocket frog', 'sumatran elephant', 'sumatran orang-utan', 'sumatran rhinoceros', 'sumatran tiger', 'sun bear', 'swan', 'tang', 'tapanuli orang-utan', 'tapir', 'tarsier', 'tasmanian devil', 'tawny owl', 'termite', 'tetra', 'thorny devil', 'tibetan mastiff', 'tiffany', 'tiger', 'tiger salamander', 'tiger shark', 'tortoise', 'toucan', 'tree frog', 'tropicbird', 'tuatara', 'turkey', 'turkish angora', 'uakari', 'uguisu', 'umbrellabird', 'vampire bat', 'vervet monkey', 'vulture', 'wallaby', 'walrus', 'warthog', 'wasp', 'water buffalo', 'water dragon', 'water vole', 'weasel', 'welsh corgi', 'west highland terrier', 'western gorilla', 'western lowland gorilla', 'whale shark', 'whippet', 'white faced capuchin', 'white rhinoceros', 'white tiger', 'wild boar', 'wildebeest', 'wolf', 'wolverine', 'wombat', 'woodlouse', 'woodpecker', 'woolly mammoth', 'woolly monkey', 'wrasse', 'x-ray tetra', 'yak', 'yellow-eyed penguin', 'yorkshire terrier', 'zebra', 'zebra shark', 'zebu', 'zonkey', 'zorse']
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
for docker in dockers_to_run:
    command = f"docker run --net=host -v /home/jetsonbot/data:/data --privileged --device=/dev/vchiq:/dev/vchiq --name {gen_name()} {docker}"

    processes.append(subprocess.Popen(command.split(" "), universal_newlines=True))

    print(f"Started '{cleanup_docker_name(docker)}'.")


def fake_func():
    while True:
        for i, process in enumerate(processes):
            if process.poll() is not None:
                print(
                    f"DOCKER LAUNCHER REPORT: process '{cleanup_docker_name(dockers_to_run[i])}' has died. \nExiting now.",
                    file=sys.stderr)
                return
        sleep(10)


fake_func()
handle_exit()
