import argparse
import p1

temp = ''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Source File location", nargs='*', action='append')
    parser.add_argument("--names", required=False, help="Removes Names", action='store_true')
    parser.add_argument("--dates", required=False, help="Removes dates", action='store_true')
    parser.add_argument("--genders", required=False, help="Removes genders and gender references", action='store_true')
    parser.add_argument("--phones", required=False, help="Removes phone numbers", action='store_true')
    parser.add_argument("--stats", type=str, required=False, help="Gives statistics for redacted files")
    parser.add_argument("--concept", type=str, required=False, help="Concept word removal", action='append')
    parser.add_argument("--output", type=str, required=True, help="Output File location")

    args = parser.parse_args()
    data = p1.input(args.input)

    if(args.names):
        data = p1.names(data)
    if(args.genders):
        data = p1.gender(data)
    if(args.dates):
        data = p1.dates(data)
    if(args.phones):
        data = p1.phonenumber(data)
    if(args.concept):
        data = p1.concept(data,args.concept)
    #print(a)
    p1.output(args.input,data,args.output)
    x = p1.input(args.input)
    if(args.stats):
       statsdict = p1.stats(x)
       p1.extractstat(statsdict)
