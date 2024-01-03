# coding: utf-8
"""
.. _l-example-protobuf:

===========================
Sérialisation avec protobuf
===========================

:epkg:`protobuf` optimise la sérialisation de deux façons.
Elle accélère l'écriture et la lecture des données et permet aussi
un accès rapide à une information précise dans désérialiser
les autres. Elle réalise cela en imposant un schéma strict de données.

L'exemple fonctionne si l'exécutable `protoc` et le package `protobuf`
ont des versions compatibles. Un message apparaîtra dans le cas contraire.

::

    protoc --version
    python -c "import google.protobuf as gp;print(gp.__version__)"

Schéma
======

On récupère l'exemple du `tutorial
<https://developers.google.com/protocol-buffers/docs/pythontutorial>`_.
"""
import os
import sys
import timeit
import struct
from io import BytesIO
from sphinx_runpython.runpython import run_cmd
import google.protobuf as gp
from google.protobuf.json_format import MessageToJson, Parse as ParseJson

schema = """
syntax = "proto2";

package tutorial;

message Person {
  optional string name = 1;
  optional int32 id = 2;
  optional string email = 3;

  enum PhoneType {
    MOBILE = 0;
    HOME = 1;
    WORK = 2;
  }

  message PhoneNumber {
    optional string number = 1;
    optional PhoneType type = 2 [default = HOME];
  }

  repeated PhoneNumber phones = 4;
}

message AddressBook {
  repeated Person people = 1;
}
"""

######################################
# Compilation
# ===========
#
# Il faut d'abord récupérer le compilateur. Cela peut se faire depuis
# le site de :epkg:`protobuf` ou sur Linux (Ubuntu/Debian)
# ``apt-get install protobuf-compiler`` pour obtenir le programme ``protoc``.


version = gp.__version__
version


#########################################
#


with open("schema.proto", "w") as f:
    f.write(schema)


# Et on peut compiler.

# In[8]:


cmd = "protoc --python_out=. schema.proto"
out, err = run_cmd(cmd=cmd, wait=True)
print(out)
print(err)


########################################
# Un fichier a été généré.


[_ for _ in os.listdir(".") if ".py" in _]


########################################


with open("schema_pb2.py", "r") as f:
    content = f.read()
print(content[:1000])


########################################
# Import du module créé
# =====================
#
# Pour utliser *protobuf*, il faut importer le module créé.


sys.path.append(".")
import schema_pb2  # noqa: E402

########################################
# On créé un enregistrement.


person = schema_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = schema_pb2.Person.HOME


########################################
#

person


########################################
# Sérialisation en chaîne de caractères
# =====================================


res = person.SerializeToString()
type(res), res


########################################
#

timeit.timeit("person.SerializeToString()", globals=globals(), number=100)


########################################
#

pers = schema_pb2.Person.FromString(res)
pers


########################################
#

pers = schema_pb2.Person()
pers.ParseFromString(res)
pers


########################################
#

timeit.timeit("schema_pb2.Person.FromString(res)", globals=globals(), number=100)


########################################
#

timeit.timeit("pers.ParseFromString(res)", globals=globals(), number=100)


########################################
# Plusieurs chaînes de caractères
# ===============================


db = []

person = schema_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = schema_pb2.Person.HOME
db.append(person)

person = schema_pb2.Person()
person.id = 5678
person.name = "Johnette Doette"
person.email = "jtdoet@example2.com"
phone = person.phones.add()
phone.number = "777-1234"
phone.type = schema_pb2.Person.MOBILE
db.append(person)


########################################
#


buffer = BytesIO()
for p in db:
    size = p.ByteSize()
    buffer.write(struct.pack("i", size))
    buffer.write(p.SerializeToString())
res = buffer.getvalue()
res


########################################
#


db2 = []
buffer = BytesIO(res)
n = 0
while True:
    bsize = buffer.read(4)
    if len(bsize) == 0:
        # C'est fini.
        break
    size = struct.unpack("i", bsize)[0]
    data = buffer.read(size)
    p = schema_pb2.Person.FromString(data)
    db2.append(p)


########################################
#

db2[0], db2[1]


########################################
# Sérialisation JSON
# ==================


print(MessageToJson(pers))


########################################
#

timeit.timeit("MessageToJson(pers)", globals=globals(), number=100)


########################################
#


js = MessageToJson(pers)
res = ParseJson(js, message=schema_pb2.Person())
res


########################################
#

timeit.timeit(
    "ParseJson(js, message=schema_pb2.Person())", globals=globals(), number=100
)
