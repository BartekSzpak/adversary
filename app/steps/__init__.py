import importlib.util
import inspect
import os
from pathlib import Path

from app.operation.step import Step


def relative_path(dunder_file, relative_path):
    directory = os.path.dirname(dunder_file)
    return os.path.join(directory, relative_path)


step_dir = Path(relative_path(__file__, ''))
# step_dir = Path(relative_path(__file__, os.path.join('app.', 'steps')))
all_steps = []
lookup_step_by_name = {}

for step_file in step_dir.iterdir():
    if step_file.is_file():
        if step_file.name.endswith('.py') and not step_file.name.startswith('__'):
            module = importlib.import_module('app.steps.' + step_file.stem, __package__)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Step) and obj != Step:
                    all_steps.append(obj)

# for some reason the below wasn't finding all the steps
all_steps.sort(key=(lambda x: x.__name__))
lookup_step_by_name = {step.__name__: step for step in all_steps}
