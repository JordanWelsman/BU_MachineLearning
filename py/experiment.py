import random

class Experiment:

    def __init__(self, num_runs):
        """
        Init function just prints a message to standard output
        """
        self.num_runs = num_runs
        print("I'm ALIVE!")
        print("Number of runs: " + str(num_runs))

    def run_experiment(self):
        """
        Runs the experiment.
        """
        results = []
        for i in range(self.num_runs):
            n = random.randint(0,9)
            print(n)
            results.append(n)
        #print(results)

if __name__ == '__main__':
    runs = 10
    an_experiment = Experiment(runs)
    an_experiment.run_experiment()

