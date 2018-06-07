

# class Configs(object):
# 	"""docstring for Configs"""
# 	def __init__(self, arg):
# 		super(Configs, self).__init__()
# 		self.arg = arg
		


START_SIM_DATE = (1990,01,01)

POSSIBLE_GENDERS = [
	'male', 'female'
]

AGE_GROUP = {
	'YOUNG': 5,
	'ADULT': 21,
	'SETTLERS': 25
}

AGE_FIRST_SCHOOL = 5

LOCATIONS = [
	'Raleigh', 
	'Atlanta',
	'Pittsburgh', 
	# 'New York',
	# 'San Francisco'
]

NUM_SCHOOLS_PER_LOCATION = 3

SCHOOL_NAMES = [
	'Allington Primary School',
	'Amherst School',
	'The Anthony Roper Primary School',
	'Ashford Oaks Community Primary School',
	'Barham CofE Primary School',
	'Barming Primary School',
	'Barn End Centre',
	'Barton Junior School',
	'Bean Primary School',
	'Beauherne Community School',
	"Brunswick House Primary School",
	"Canterbury Road Primary School",
	"Canterbury St Peter's Methodist Primary School",
	"Capel Primary School",
	"Capel-le-Ferne Primary School",
	"Cecil Road Primary School",
	"Challenger Centre",
	"Chantry Primary School",
	"Cheriton Primary School",
	"Chevening St Botolph's CofE Primary School",
	"Chiddingstone CofE Primary School",
	"Chilham St Mary's CofE Primary School",
	"Chilton Primary School",
	"Colliers Green CofE Primary School",
	"Coxheath Primary School",
	"Cranbrook CofE Primary School"
	"Crockham Hill CofE Primary",
	"Culverstone Green Primary School",
	"Dame Janet Infant School",
	"Dame Janet Junior School",
	"Darenth Community Primary School",
	"The Discovery School",
	"Ditton CofE Junior School",
	"Downs View Infants School",
]


HOSPITAL_NAMES = [
	'Citrus Medical Center',
	'Clemency Medical Clinic',
	'Silver Birch Community Hospital',
	'Grand Mountain Hospital Center',
	'Golden Valley Hospital',
	'Fairbanks Clinic',
	'Horizon Medical Clinic',
	'Grand Mountain Community Hospital',
	'Featherfall Hospital Center',
	'Green Hill Hospital',
	'Pine Valley Hospital',
	'Sapphire Lake Medical Clinic',
	'Rosewood Medical Clinic',
	'Wellness Medical Clinic',
	'Pioneer Clinic',
	'Spring Forest Hospital',
	'Freeman Clinic',
	'Castle Hospital',
	'Tranquility Hospital',
	'Hill Crest Hospital Center',
	'Silver Pine Clinic',
	'Summer Springs Hospital',
	'Lakeside Clinic',
	'Fairmont Medical Center',
	'Progress Medical Clinic',
	'Oak Valley Community Hospital',
	'Rose Medical Center',
	'Mountain View General Hospital',
	'Silver Wing Hospital Center',
	'Griffin Hospital Center'
]


def find_all_changed_facts_for_person_index(world, index):
	for fact in world.living_population[index].knowledge.facts.values():
	    if fact.historical_opinions:
	        print fact.name, ":", fact.opinion
	        print "\t \tBefore: ", fact.historical_opinions


def find_most_changed_fact(world):
    current_max = 0
    info = None
    npc = None
    for person in world.living_population: 
        for fact in person.knowledge.facts.values(): 
            if len(fact.historical_opinions) > current_max:
                current_max = len(fact.historical_opinions)
                info = fact
                npc = person
    return npc.census_index-1, info