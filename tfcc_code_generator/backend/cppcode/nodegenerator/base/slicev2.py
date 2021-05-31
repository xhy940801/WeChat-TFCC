# Copyright 2021 Wechat Group, Tencent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ir.node
from backend.cppcode.nodegenerator.nodegenerator import NodeGenerator


class SliceV2(NodeGenerator):
    @classmethod
    def accept(cls, node: ir.node.Node):
        return isinstance(node, ir.node.base.SliceV2)

    @property
    def code(self):
        if self.inputs[1].is_signed():
            return "auto {outputs[0]} = tfcc::helper::base::slice({inputs[0]}, {node.axis}, static_cast<int64_t>({inputs[1]}), static_cast<int64_t>({inputs[2]}));\n".format(
                **self.fmt_dict
            )
        else:
            return "auto {outputs[0]} = tfcc::base::slice({inputs[0]}, {node.axis}, {inputs[1]}, {inputs[2]});\n".format(
                **self.fmt_dict
            )