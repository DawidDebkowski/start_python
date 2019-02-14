import argparse


parser = argparse.ArgumentParser(description='Powiedz: Witam serdecznie pana --name')
parser.add_argument('--name', type=str, help='Pańskie imię proszę Pana!')


args = parser.parse_args()

print("Witam serdzecznie Pana " + args.name)
