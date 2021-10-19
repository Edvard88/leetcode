# from collections import deque
#
# G = {0: [1, 6],
#      1: [2, 3],
#      2: [1],
#      3: [1, 4],
#      4: [3, 5],
#      5: [4, 6],
#      6: [5, 0]
#      }
#
#
#
# def bfs(start_point: int) -> None:
#     """ Search in graph BFS algorithm
#
#     :param start_point:
#     :return: None
#     """
#     search_q  = deque()
#     search_q += G[start_point]
#     visited = []
#
#     while search_q:
#         start_point = search_q.popleft()
#         if not start_point in visited:
#             search_q += G.get(start_point)
#             visited.append(start_point)
#             print("search_q", search_q)
#             print("visited", visited)
# #bfs(0)
# #
# #

G =  {    1 : [3, 2, 4],
          2 : [],
          3 : [5,6],
          4 : [],
          5 : [],
          6 : []
    }

def maxDepth1(G_new):
    print("2222222222")
    max_depth = 1

    list_node = G_new[1]
    visited = []
    i = 1
    print("11111111111")
    print(list_node)
    while len(list_node)!=0:
        print("Before print", list_node[0])
        if len(G_new[list_node[0]])!=0:
            print("After print",list_node[0])
            max_depth+=1
            print("max_depth", max_depth)
            visited.extend(G_new[list_node[0]])
            print("Before pop", list_node)
            list_node.pop(0)

            print("After pop", list_node)
            list_node.extend([G_new[list_node[0]]])
            print("After extend", list_node)

            i+=1
    print("i", i)
    print("visited", visited)
    print("list_node", list_node)
    print("max_depth", max_depth)

maxDepth1(G)

