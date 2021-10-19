G_object_1 =  {    1 : [3, 2, 4],
          2 : [],
          3 : [5,6],
          4 : [],
          5 : [],
          6 : []
    }



G_object_2 =  {
          1 : [2, 3, 4, 5],
          2 : [],
          3 : [6,7],
          4 : [8],
          5 : [9,10],
          6 : [],
          7 : [11,14],
          8 : [12],
          9 : [13],
          10 : [],
          11 : [14],
          12 : [],
          13 : [],
          14 : []
     }




def maxDepth1(G):
    print("Начало функции")
    max_depth = 1

    list_node = G[1]
    visited = []

    i = 1
    print("List_node перед циклом while:", list_node)
    while len(list_node)!=0:
        print("Выполнилось условие перед if")
        print("List_node перед if:", list_node)
        print("G[list_node[0]] перед if равно", G[list_node[0]])
        if len(G[list_node[0]]) != 0:
            print("G[list_node[0]] посел if равно", G[list_node[0]])
            print("List_node после if:", list_node)

            max_depth += 1
            print("max_depth", max_depth)

        visited.extend([list_node[0]])

        list_node.extend(G[list_node[0]])
        print("List_node после extend:", list_node)

        print("List_node перед pop:", list_node)
        list_node.pop(0)
        print("List_node после pop:", list_node)

        print("==========================")
    max_depth += 1

    print("visited", visited)
    print("list_node", list_node)
    print("max_depth", max_depth)

#maxDepth1(G_object_2)

def bfs_with_distance()


