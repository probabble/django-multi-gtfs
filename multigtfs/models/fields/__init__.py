#
# Copyright 2012-2014 John Whitlock
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from seconds import Seconds, SecondsField

# pyflakes be quiet
__classes__ = Seconds
__fields__ = SecondsField

try:
    from south.modelsinspector import add_introspection_rules
except ImportError:  # pragma: no cover
    # south is not required
    pass
else:
    add_introspection_rules([], ['^django\.contrib\.gis'])
