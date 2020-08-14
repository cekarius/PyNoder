import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from pynoder.graph_view import GraphView
from pynoder.graph_view_widget import GraphViewWidget
from pynoder.node import Node
from pynoder.port import InputPort, OutputPort, IOPort

form_class = uic.loadUiType("addNodesMain.ui")[0]

widget = 0
graph = 0

class MyMainWindow(QMainWindow, form_class):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.nodes_widget = NodesWidget(self) 
        self.setCentralWidget(self.nodes_widget) 

        self.setupUi(self)
        
        self.addAddNode.clicked.connect(NodesWidget.add_node)
        self.addSubNode.clicked.connect(NodesWidget.sub_node)


class NodesWidget(QWidget):

    def __init__(self, parent):        
        super(NodesWidget, self).__init__(parent)
        global graph
        global widget
        widget = GraphViewWidget()
        graph = GraphView(parent=widget)

        widget.setGraphView(graph)
        widget.setWindowTitle('Graph')
        widget.show()
    
    def add_node(self):
        global graph
        global widget
        
        node = Node(graph, 'Add')
        node.addPort(InputPort(node, graph, 'Input', QColor(128, 170, 170, 255), 'Number'))
        node.addPort(InputPort(node, graph, 'Input', QColor(128, 170, 170, 255), 'Number'))
        node.addPort(OutputPort(node, graph, 'Output', QColor(32, 255, 32, 255), 'Number'))
        node.setNodePos(QPointF(100, 0))

        graph.addNode(node)
        
        widget.show()

    def sub_node(self):
        global graph
        global widget
        
        node = Node(graph, 'Subtract')
        node.addPort(InputPort(node, graph, 'Input', QColor(128, 170, 170, 255), 'Number'))
        node.addPort(InputPort(node, graph, 'Input', QColor(128, 170, 170, 255), 'Number'))
        node.addPort(OutputPort(node, graph, 'Output', QColor(32, 255, 32, 255), 'Number'))
        node.setNodePos(QPointF(100, 0))

        graph.addNode(node)
        
        widget.show()
print(sys.executable)
app = QApplication(sys.argv)
main = MyMainWindow()
main.show()
sys.exit(app.exec_())
