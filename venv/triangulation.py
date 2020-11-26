from dcel import vertex, hedge, face, DCEL

def triangulateFace(f,D):
    oldEdges=f.outerComponent.loop()
    firstEdge=f.outerComponent;
    secondEdge=f.outerComponent.next;
    while secondEdge!=f.outerComponent.previous:
        newFace=D.createFace()
        newFirst=D.createHedge()
        newSecond=D.createHedge()
        newEdge=D.createHedge()
        newEdgeTwin=D.createHedge()
        newFace.setTopology(newEdge)
        newFirst.setTopology(firstEdge.origin,firstEdge.twin,newFace,newSecond,newEdge)
        newSecond.setTopology(secondEdge.origin, secondEdge.twin, newFace, newEdge, newFirst)
        newEdge.setTopology(secondEdge.next.origin,newEdgeTwin,newFace,newFirst,newSecond)
        newEdgeTwin.setTopology(firstEdge.origin, newEdge,None, None, None)
        firstEdge=newEdgeTwin
        secondEdge=secondEdge.next
    for edge in oldEdges:
        D.remove(edge)
    for edge in D.hedgeList:
        if edge.next==None:
            D.remove(edge)
    D.remove(f)    
    return D

def triangulate(D):
    i=0
    while i<len(D.faceList):
        f=D.faceList[i]
        count=0
        for ver in f.loopOuterVertices():
            count=count+1
        if count>3:
            D=triangulateFace(f,D)
        else:
            i=i+1
    return D