from actor import Actor


class Enemy(Actor):

    def __init__(self, level_map, coord, actor_id):

        Actor.__init__(self, level_map, coord, actor_id)
        # self.ai_component =
