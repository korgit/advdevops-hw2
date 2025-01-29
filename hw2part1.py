#Homework 2, part 1
def argparser():
    import sys
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        print("No arguments provided, please provide a filename to read")
        print(f"Usage: {sys.argv[0]} filename")
        return -1

def find_sum(fname):
    sum = 0
    try:
        with open(fname) as file:
            lines = file.readlines()
            for line in lines:
                for fchar in line:
                    if fchar.isdigit():
                        firstdigit = fchar
                        break
                for lchar in reversed(line):
                    if lchar.isdigit():
                        lastdigit = lchar
                        break
                sum += int(fchar + lchar)
        return sum
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("You don't have permission to access this file.")
    except Exception as e:
        print("An error occurred:", e)
    return -1
    

if __name__ == "__main__":
    ret = argparser()
    if ret != -1:
        sum = find_sum(ret)
        if sum != -1:
            print(f"Sum of all calibration values is: {sum}")
        else:
            print("Error occured")

    
        

