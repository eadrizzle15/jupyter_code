# election app

from election import *

def main():
    election = Election()
    election.registerPeople(2)
    election.vote()

main()