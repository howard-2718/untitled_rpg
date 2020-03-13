import config


class Entity:
    # Players and enemies inherit from this entity class
    def __init__(self, name, lvl, xp, next_lvl_req,
                 hp, mp, p_atk, p_def, m_atk, m_def,
                 hp_grow, mp_grow, p_atk_grow, p_def_grow, m_atk_grow, m_def_grow,
                 earth_res, water_res, fire_res, air_res, dark_res, light_res, null_res, skills):
        # Everything except the name should be an int, and next_lvl_req should be an array...? maybe.
        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.xp_total = xp
        self.next_lvl_req = next_lvl_req

        self.cur_hp = hp
        self.hp = hp
        self.cur_mp = mp
        self.mp = mp

        self.p_atk = p_atk
        self.p_def = p_def
        self.m_atk = m_atk
        self.m_def = m_def

        self.hp_grow = hp_grow
        self.mp_grow = mp_grow
        self.p_atk_grow = p_atk_grow
        self.p_def_grow = p_def_grow
        self.m_atk_grow = m_atk_grow
        self.m_def_grow = m_def_grow

        self.earth_res = earth_res
        self.water_res = water_res
        self.fire_res = fire_res
        self.air_res = air_res
        self.dark_res = dark_res
        self.light_res = light_res
        self.null_res = null_res

        # TODO: skills
        self.skills = []
        for skill_id in skills:
            self.skills.append(config.skills[skill_id])

    def print_stats(self):
        print(self.name + "'s Stats")  # TODO: get rid of possible "s's" occurring somehow
        print("Level: " + str(self.lvl))
        print("Experience: " + str(self.xp_total))
        print("HP: " + str(self.cur_hp) + "/" + str(self.hp))
        print("MP: " + str(self.cur_mp) + "/" + str(self.mp))
        print("Physical Attack: " + str(self.p_atk))
        print("Physical Defense: " + str(self.p_def))
        print("Magical Attack: " + str(self.m_atk))
        print("Magical Defense: " + str(self.m_def))
        print("Resistances: ")
        print("Earth: " + str(self.earth_res))
        print("Water: " + str(self.water_res))
        print("Fire: " + str(self.fire_res))
        print("Air: " + str(self.air_res))
        print("Dark: " + str(self.water_res))
        print("Light: " + str(self.earth_res))
        print("Null: " + str(self.null_res))

    def level_up(self):
        if self.xp >= self.next_lvl_req[self.lvl - 1]:
            self.lvl += 1

            self.hp += self.hp_grow
            self.cur_hp += self.hp_grow
            self.mp += self.mp_grow
            self.cur_mp += self.mp_grow

            self.p_atk += self.p_atk_grow
            self.p_def += self.p_def_grow
            self.m_atk += self.m_atk_grow
            self.m_def += self.m_def_grow
            self.xp -= self.next_lvl_req[self.lvl - 2]
        else:
            print("Insufficient XP!")
            return "not enough xp"

    def level_down(self):  # god knows why you'd want to do this, but the option is there
        if not self.lvl <= 1:
            self.lvl -= 1
            self.hp -= self.hp_grow
            self.cur_hp -= self.hp_grow
            self.mp -= self.mp_grow
            self.cur_mp -= self.mp_grow
            self.p_atk -= self.p_atk_grow
            self.p_def -= self.p_def_grow
            self.m_atk -= self.m_atk_grow
            self.m_def -= self.m_def_grow
            self.xp += self.next_lvl_req[self.lvl]
        else:
            print("Cannot do that!")
            return "level too small"

    def use_skill(self, skill):
        pass


class Player(Entity):
    def __init__(self, name, lvl, xp, next_lvl_req,
                 hp, mp, p_atk, p_def, m_atk, m_def,
                 hp_grow, mp_grow, p_atk_grow, p_def_grow, m_atk_grow, m_def_grow,
                 earth_res, water_res, fire_res, air_res, dark_res, light_res, null_res, skills):
        super().__init__(name, lvl, xp, next_lvl_req,
                         hp, mp, p_atk, p_def, m_atk, m_def,
                         hp_grow, mp_grow, p_atk_grow, p_def_grow, m_atk_grow, m_def_grow,
                         earth_res, water_res, fire_res, air_res, dark_res, light_res, null_res, skills)

    def print_stats(self):
        super().print_stats()

    def level_up(self):
        super().level_up()

    def level_down(self):
        super().level_down()

    def display_stats_battle(self):
        return self.name + " ------- HP: " + str(round(self.cur_hp)) + "/" + str(self.hp) + "  MP: " + \
               str(self.cur_mp) + "/" + str(self.mp)


class Enemy(Entity):
    def __init__(self, name, lvl, xp, next_lvl_req,
                 hp, mp, p_atk, p_def, m_atk, m_def,
                 hp_grow, mp_grow, p_atk_grow, p_def_grow, m_atk_grow, m_def_grow,
                 earth_res, water_res, fire_res, air_res, dark_res, light_res, null_res, skills, xp_given):
        super().__init__(name, lvl, xp, next_lvl_req,
                         hp, mp, p_atk, p_def, m_atk, m_def,
                         hp_grow, mp_grow, p_atk_grow, p_def_grow, m_atk_grow, m_def_grow,
                         earth_res, water_res, fire_res, air_res, dark_res, light_res, null_res, skills)

        self.xp_given = xp_given  # Should be a base amount which is scaled according to level somehow

    def print_stats(self):
        super().print_stats()

    def level_up(self):
        super().level_up()

    def level_down(self):
        super().level_down()

    def display_stats_battle(self):
        return self.name + " ------- HP: " + str(round(self.cur_hp)) + "/" + str(self.hp)
