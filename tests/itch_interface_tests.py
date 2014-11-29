# Run all tests from basedir with `nosetests`. Don't run locally, imports fail
from roulette.game import Game
import roulette.itch_interface as itch_interface



def test_remove_duplicates_happy():
	assert False


if __name__ == '__main__':
	nose.main()