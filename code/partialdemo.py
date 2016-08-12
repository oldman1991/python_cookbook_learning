# coding=utf-8
from functools import partial


# def parm(a, b,c):
#     return (a,b,c)
#
# s1 = partial(parm, 1,132)
# print(s1(13))





# import math
#
# points = [(1,2),(3,4),(5,6),(7,8)]
# def distance(p1,p2):
#     x1,y1=p1
#     x2,y2=p2
#     return math.hypot(x2-x1,y2-y1)
#
# pt=(4,3)
# points.sort(key=partial(distance,pt))
# print(points)




def output_result(result, log=None):
    if log is not None:
        log.debug('Got:%r', result)
#A sample function
def add(x,y):
    return x+y

if __name__=="__main__":
    import logging
    from multiprocessing import Pool
    logging.basicConfig(level=logging.DEBUG)
    log=logging.getLogger('test')
    p = Pool()
    p.apply_async(add,(3,4),callback=partial(output_result,log=log))
    p.close()
    p.join()
