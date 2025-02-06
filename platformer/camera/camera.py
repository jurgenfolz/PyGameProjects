class Camera:
    def __init__(self, screen_width, screen_height, world_width, world_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.world_width = world_width
        self.world_height = world_height

        self.x = 0
        self.y = 0

    def update(self, target_x, target_y):
        """
        Center camera on (target_x, target_y), then clamp to world bounds.
        """
        # Center on target
        self.x = target_x - self.screen_width // 2
        self.y = target_y - self.screen_height // 2

        # Clamp so we don't see outside the world
        if self.x < 0:
            self.x = 0
        if self.x + self.screen_width > self.world_width:
            self.x = self.world_width - self.screen_width

        if self.y < 0:
            self.y = 0
        if self.y + self.screen_height > self.world_height:
            self.y = self.world_height - self.screen_height

    def apply(self, world_x, world_y):
        """
        Convert a world (x, y) into screen coordinates, using the camera offset.
        """
        return (world_x - self.x, world_y - self.y)
