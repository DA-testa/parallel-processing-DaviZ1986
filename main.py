# python3
#Dāvis Zommers 221RDB150
import heapq as hq
def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(0, i) for i in range(n)]
    hq.heapify(threads)
    threads_eta = []
    print(len(threads_eta))
    for i in range(m):
        time = data[i]
        moment, thread = hq.heappop(threads)
        output.append((thread, moment))
        hq.heappush(threads, (moment + time, thread))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    line = list(map(int, input().split()))
    n = int(line[0])
    m = int(line[1])
    data = list(map(int, input().split()))
    #n = 0
    #m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    #data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i, j in result:
        print(i, j)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()

