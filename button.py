import pygame.font


class Button:

    def __init__(self, ai_settings, screen, msg):
        """Initializes button attributes"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (2, 23, 27)
        self.font = pygame.font.SysFont("Consolas", 48, True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        #self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.centerx = self.rect.centerx + 6
        self.msg_image_rect.centery = self.rect.centery

    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)