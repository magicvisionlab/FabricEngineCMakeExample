#
# Fabric Engine 1.12.0
# HelloWorld EDK Sample
#
# Copyright 2010-2014 Fabric Software Inc. All rights reserved.
#

import os
if 'FABRIC_EXTS_PATH' in os.environ:
  os.environ['FABRIC_EXTS_PATH'] = os.pathsep.join(['.', os.environ['FABRIC_EXTS_PATH']])
else:
  os.environ['FABRIC_EXTS_PATH'] = '.'

import FabricEngine.Core as fabric
fabricClient = fabric.createClient();

opSource = """
require HelloWorld;

operator entry(io String string) {
  report("KL: Enter entry");
  string = GetHelloWorldString();
  report("KL: GetHelloWorldString returned: " + string);
  report("KL: Leave entry");
}
"""
op = fabricClient.DG.createOperator("op")
op.setSourceCode(opSource)
op.setEntryPoint("entry")

b = fabricClient.DG.createBinding()
b.setOperator(op)
b.setParameterLayout(['self.string'])

node = fabricClient.DG.createNode("node")
node.addMember("string", "String")
node.bindings.append(b)
node.evaluate()
print "Python got: " + node.getData("string", 0)

fabricClient.close()
