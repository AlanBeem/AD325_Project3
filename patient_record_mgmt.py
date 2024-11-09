from binary_search_tree import *
import graphviz #
import csv


class PatientRecord:
    def __init__(self, patiend_id, name, age, diagnosis, blood_pressure, pulse, body_temperature):
        self.patiend_id = patiend_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.blood_pressure = blood_pressure
        self.pulse = pulse
        self.body_temperature = body_temperature
    
    def __str__(self) -> str:
        return f"Patient ID: {self.patiend_id}, Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}, Blood Pressure: {self.blood_pressure}, Pulse: {self.pulse}, Body Temperature: {self.body_temperature}"


class PatientRecordManagementSystem:
    def __init__(self):
        self.bst = BinarySearchTree()
        self.node_labels = []

    class BloodPressure:
        def __init__(self, diastolic, systolic):
            self.diastolic = diastolic
            self.systolic = systolic
        
        def __repr__(self) -> str:  # Determines return for this in PatientRecord __str__
            return f"{self.diastolic}/{self.systolic}"

    def add_patient_record(self, patient_id, name, age, diagnosis, blood_pressure, pulse, body_temperature) -> None:
        # O(logN)
        """converts arguments into appropriate data types, where applicable."""
        self.bst.insert(Node(int(patient_id), PatientRecord(int(patient_id), name, int(age), diagnosis,
                        PatientRecordManagementSystem.BloodPressure(blood_pressure.split('/')[0], blood_pressure.split('/')[1]),
                        int(pulse), float(body_temperature))))

    def search_patient_record(self, patient_id):  # O(logN)
        return self.bst.search(patient_id)

    def delete_patient_record(self, patient_id):  # O(logN)
        record = self.bst.search(patient_id)                  # = O(logN)
        if record is not None:
            record = record.value
        self.bst.remove(patient_id)                           #   + O(logN)
        return record

    def display_all_records(self, traversal_function=inorder_traversal):  # O(N)
        """Displays all patient records in the BST using inorder traversal."""
        for node in traversal_function(self.bst.root):
            print(node.value)

    def build_tree_from_csv(self, file_path):  # O(N*logN)
        with open(file_path, 'r') as open_file:  # =
            file_reader = \
                csv.DictReader(open_file, fieldnames=['PatientID','Name', 'Age',
                                                      'Diagnosis', 'BloodPressure',
                                                      'Pulse', 'BodyTemperature'])  # next(open_file).split(',')
            next(file_reader)
            for row in file_reader:              #  O(N) * O(logN)
                self.add_patient_record(row['PatientID'], row['Name'], row['Age'], row['Diagnosis'], row['BloodPressure'], row['Pulse'], row['BodyTemperature'])
        open_file.close()

   ## graphviz code provided                                                                # # #
    # # Mac install how-to:
    # #  install graphviz executables to a folder (run installation .pkg),
    # #  add alias of folder to usr/local/bin,
    # #  pip install graphviz.
    def visualize_tree(self):  # O(N)
        """Visualizes the BST using Graphviz."""
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.bst.root)  # recursive
        return dot

    def _add_nodes(self, dot, node):  # recurses to O(N)
        """a helper method that recursively adds nodes and edges to the Graphviz object."""
        if node:
            self.node_labels.append(node.key)
            dot.node(str(node.key), f"{node.key}: {node.value.name}")  # value is PatientRecord
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)  # recursion
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)  # recursion
   ##                                                                                       # # #

