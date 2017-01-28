import sys
from PyQt5 import QtGui, QtWidgets, QtCore

from pynoder.graph_view import GraphView
from pynoder.graph_view_widget import GraphViewWidget
from pynoder.node import Node
from pynoder.port import InputPort, OutputPort, IOPort

app = QtWidgets.QApplication(sys.argv)

widget = GraphViewWidget()
graph = GraphView(parent=widget)

node1 = Node(graph, 'Short')
node1.addPort(InputPort(node1, graph, 'InPort1', QtGui.QColor(128, 170, 170, 255), 'MyDataX'))
node1.addPort(InputPort(node1, graph, 'InPort2', QtGui.QColor(128, 170, 170, 255), 'MyDataX'))
node1.addPort(OutputPort(node1, graph, 'OutPort', QtGui.QColor(32, 255, 32, 255), 'MyDataY'))
node1.addPort(IOPort(node1, graph, 'IOPort1', QtGui.QColor(32, 255, 32, 255), 'MyDataY'))
node1.addPort(IOPort(node1, graph, 'IOPort2', QtGui.QColor(32, 255, 32, 255), 'MyDataY'))
node1.setNodePos(QtCore.QPointF(-100, 0))

graph.addNode(node1)

node2 = Node(graph, 'ReallyLongLabel')
node2.addPort(InputPort(node2, graph, 'InPort1', QtGui.QColor(128, 170, 170, 255), 'MyDataY'))
node2.addPort(InputPort(node2, graph, 'InPort2', QtGui.QColor(128, 170, 170, 255), 'MyDataX'))
node2.addPort(OutputPort(node2, graph, 'OutPort', QtGui.QColor(32, 255, 32, 255), 'MyDataY'))
node2.addPort(IOPort(node2, graph, 'IOPort1', QtGui.QColor(32, 255, 32, 255), 'MyDataY'))
node2.addPort(IOPort(node2, graph, 'IOPort2', QtGui.QColor(32, 255, 32, 255), 'MyDataY'))
node2.setNodePos(QtCore.QPointF(100, 0))

graph.addNode(node2)
graph.connectPorts(node1, 'OutPort', node2, 'InPort1')

widget.setGraphView(graph)
widget.show()

sys.exit(app.exec_())
