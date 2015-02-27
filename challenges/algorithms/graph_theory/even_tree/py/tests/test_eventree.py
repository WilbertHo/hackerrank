from nose.tools import eq_
import eventree


def test_buildgraph():
    eq_(eventree.build_graph([[2, 1], [3, 1], [4, 3], [5, 2],
                              [6, 1], [7, 2], [8, 6], [9, 8],
                              [10, 8]]),
        {1: [2, 3, 6], 2: [5, 7], 3: [4], 6: [8], 8: [9, 10], })

    eq_(eventree.build_graph([[2, 1]]), {1: [2]})


def test_subtree_count():
    graph = eventree.build_graph([[2, 1], [3, 1], [4, 3], [5, 2],
                                  [6, 1], [7, 2], [8, 6], [9, 8],
                                  [10, 8]])
    eq_(eventree.subtree_count(graph, 1), 10)
    eq_(eventree.subtree_count(graph, 2), 3)
    eq_(eventree.subtree_count(graph, 6), 4)
    eq_(eventree.subtree_count(graph, 9), 1)
    eq_(eventree.subtree_count(graph, 10), 1)

    graph = eventree.build_graph([[2, 1]])
    eq_(eventree.subtree_count(graph, 1), 2)
    eq_(eventree.subtree_count(graph, 2), 1)
