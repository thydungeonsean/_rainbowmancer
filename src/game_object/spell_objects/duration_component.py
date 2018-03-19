

class DurationComponent(object):

    def __init__(self, owner, duration):

        self.owner = owner
        self.duration = duration
        self.complete = False

    def is_complete(self):
        return self.complete

    def end(self):
        self.complete = True
        self.owner.level_map.object_manager.request_update()

    def over(self):
        return self.duration <= 0

    def tick(self):
        self.duration -= 1
