import os, time

TEXT_SPEED = 0.02  # Adjust this value to change the speed of the text

def print_with_delay(text, delay):
    print(''.join(char for char in text), end='', flush=True)
    time.sleep(delay)

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def start_game(hero_name):
    lore = [
        f"""
Welcome to the realm of the Ancient Kingdom. You are a brave hero, known as {hero_name}.
The legend of the ancient dragon has haunted your dreams for as long as you can remember.
        """,
        """ 
The tales tell of a beast of unimaginable size and power, its scales as dark as obsidian, 
and its roar capable of shaking mountains.
        """,
        """ 
The dragon has plagued the land for generations, leaving ruin in its wake and 
terror in the hearts of all who know its name.
        """,
        """
But you are not like the others. You are driven by a deep sense of duty—or perhaps vengeance—to end the dragon's reign and bring peace to the realm. 
        """,
        """   
Your journey will not be easy; you will face countless dangers, from cunning goblins in the forests to sinister wizards in their towers.
        """,
        """
Each step will bring you closer to the final battle, yet every step will also test your courage and resolve.
        """,
        """
The path ahead is shrouded in mystery, but your goal is clear: slay the dragon and restore hope to the world. Gather your strength, equip your weapons, and step into the unknown. Your journey begins now.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()

def goblinIntro():
    lore = [
        f"""
With the resolve of a seasoned warrior, you set off into the wilderness, your heart pounding with a mix of anticipation and trepidation. 
The trees tower above, their dense canopies blocking out the sun and casting the forest into a permanent twilight. 
It's the kind of place where danger lurks behind every shadow, and you keep your hand on your weapon, ready for anything.
        """,
        """
As you navigate the winding path, a faint rustling echoes through the underbrush. You pause, listening intently. 
The rustling grows louder, accompanied by a low, guttural growl that sends shivers down your spine. 
From the corner of your eye, you catch a glimpse of movement—something small, yet agile. 
It darts through the foliage with alarming speed, closing the distance between you in an instant.
        """,
        """
A goblin lunges from the shadows, its crude blade glistening with malice. The creature's eyes are a sickly yellow, 
filled with a mixture of cunning and rage. Its skin, a mottled green, is covered in grime and scars from countless skirmishes. 
This is no ordinary goblin—it's a scout, one of the tribe's most aggressive and deadly warriors, tasked with hunting down intruders like you.
        """,
        """
The goblin snarls and charges, swinging its blade with reckless abandon. This is your first battle, the opening test of your journey. 
Your instincts kick in, and you prepare to meet the goblin's assault with all the skill and courage you can muster. 
If you falter now, your quest may end before it truly begins. The forest holds many secrets, 
but you are determined to uncover them all, one battle at a time.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()


def goblinOutro():
    lore = [
        f"""
The goblin falls to the ground with a final, guttural groan, its weapon clattering beside it. 
The forest seems to hold its breath as if acknowledging the end of the skirmish. 
Silence settles over the trees, punctuated only by the distant call of a bird and the rustling of leaves in the wind.
        """,
        """
You catch your breath and scan the area, alert for any signs of reinforcements. None come. The threat has passed—for now. 
You wipe your dagger clean and step over the fallen goblin, knowing this victory is but a small step on a long journey. 
Ahead, the forest stretches into darkness, hinting at greater challenges to come.
        """,
        """
With renewed determination, you press on, each step bringing you closer to your ultimate goal. 
The dragon awaits, but first, you must navigate the dangers of the wild. As you move forward, you know one thing for certain: 
this victory has made you stronger, and nothing will stop you from reaching the end of your quest.
        """,
        """
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()

def ogreIntro():
    lore = [
        f"""
After the goblin encounter, you venture deeper into the forest, the air thick with the scent of pine and damp earth. 
The underbrush grows denser, making it difficult to see far ahead. 
Every crackling twig and distant call makes you grip your weapon tighter, aware that this forest holds more dangers than just goblins.
        """,
        """
As you navigate through the maze of trees, a low, rhythmic thumping resonates through the ground. 
It feels like the heartbeat of the forest itself, growing stronger with each step. You slow your pace, listening carefully, 
and the source of the noise becomes clear—a heavy footfall, deliberate and slow.
        """,
        """
You round a bend, and there, towering above the trees, is an ogre. Its massive frame is clad in tattered furs, 
its skin a mottled shade of grayish-green. The ogre’s eyes are small but filled with a primal rage, 
and its oversized club rests on its shoulder, ready to swing at any moment. 
It's clear that this creature has been tasked with guarding this part of the forest, and you're intruding on its territory.
        """,
        """
The ogre lets out a roar that shakes the treetops, warning you to leave or face its wrath. But you know there's no turning back now. 
The path to the dragon runs through this forest, and the ogre is a formidable obstacle on your journey. 
You tighten your grip on your weapon and prepare for another battle, knowing that defeating this hulking beast will require all your skill and cunning. 
It's time to face the ogre and continue your journey toward the ultimate goal—slaying the dragon.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()

def ogreOutro():
    lore = [
        f"""
The ogre collapses with a thunderous crash, sending leaves and dust flying in all directions. 
Its club slips from its grasp and lands heavily at your feet, a final reminder of the fierce battle you just endured. 
The forest, once filled with the ogre's roars, falls eerily silent, as if even nature itself is stunned by your victory.
        """,
        """
You stand over the defeated beast, your breath coming in steady, deep gulps as the adrenaline fades. 
This encounter could have ended much differently, but your skill and courage prevailed. 
Though your journey is far from over, you've proven to yourself that you can overcome even the mightiest foes.

        """,
        """
Taking a moment to collect yourself, you glance around, ensuring there are no other threats lurking in the shadows. 
The path ahead seems a little clearer now, and the forest feels a bit less hostile. 
Yet, you know this is just the beginning—the road to slaying the dragon is long and fraught with danger.
        """,
        """
As you step over the ogre's massive form, you feel a sense of accomplishment and a growing resolve. 
You've bested a guardian of the forest, and with each challenge you conquer, you draw closer to your ultimate goal. 
The dragon awaits, and you are determined to meet it with the same tenacity that carried you through this battle.

        """
        """
With renewed determination, you continue your journey, knowing that each victory, each step forward, 
brings you one step closer to your destiny. The forest stretches before you, and you stride into its depths, ready for whatever comes next.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()


def trollIntro():
    lore = [
        f"""
Emerging from the dense forest, you find yourself at the edge of a wide ravine. 
A bridge spans the chasm, its weathered stone arches reaching toward a looming tower on the other side. 
The tower is a silhouette against the setting sun, its spires rising into the darkening sky. 
It's a place of mystery, shrouded in legend, rumored to be the home of a powerful wizard.
        """,
        """
You take a cautious step toward the bridge, but your movement stirs something beneath it. 
A low growl reverberates from the shadows, and then, with a slow and deliberate motion, a hulking troll emerges. 
It's a massive creature, with thick, leathery skin and tusks protruding from its lower jaw. 
The troll's eyes are a dull yellow, full of malice, and its movements are slow but deliberate. 
It's clear this beast guards the bridge, and it doesn't seem interested in letting anyone pass.
        """,
        """
The troll steps forward, its heavy footfalls shaking the ground. It holds a crude club, 
a splintered log that looks as if it could shatter stone with a single swing. 
The creature stares at you with a mixture of curiosity and hunger, its snarl deepening as it steps onto the bridge, blocking your path.
        """,
        """
To reach the tower, you'll have to confront the troll and somehow defeat it. 
This is a crucial point in your journey—a test of strength, skill, and cunning. 
The troll's sheer size and power make it a formidable opponent, but you're not without your own skills and determination.
        """
        """
As you grip your weapon, preparing for the battle ahead, you know that defeating the troll is the only way 
to continue your journey and uncover the secrets within the tower. With a deep breath, you step forward onto the bridge, 
ready to face the troll and prove that you are not one to be deterred by any guardian, no matter how fearsome.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()

def trollOutro():
    lore = [
        f"""
With a final blow, the troll collapses to the ground, its massive body sending shockwaves through the bridge. 
Dust and debris settle slowly, and the echo of its fall fades into the surrounding ravine. 
As the creature lies motionless, the air grows still, the oppressive weight of the troll's presence lifting.
        """,
        """
You stand over the defeated beast, your breathing heavy but steady. The bridge, once a domain of terror, is now yours to cross. 
Beyond it, the mysterious tower looms, its silhouette stark against the darkening sky. 
The tower's spires seem to reach toward the heavens, but its base is shrouded in shadows, offering no clues to what lies within.
        """,
        """
Taking a moment to gather yourself, you look across the bridge. 
The tower is your next destination, but it's clear that reaching it won't be easy. 
The presence of a guardian troll suggests the tower holds secrets, perhaps guarded by other creatures or traps. 
Yet your victory over the troll is a sign that you have the strength and skill to overcome these challenges.
        """,
        """
As you walk toward the tower, each step brings you closer to the answers you seek—and to the ultimate goal of slaying the dragon. 
The road ahead is uncertain, but you're ready to face whatever lies within the tower's ancient stone walls. 
With your weapon at the ready, you cross the bridge, determined to unravel the mysteries that await and continue your journey toward destiny.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()


def wizardIntro():
    lore = [
        f"""
Crossing the bridge, you step into the tower, its heavy wooden door groaning as it swings open. 
The interior is dimly lit, with narrow shafts of light piercing through cracks in the stone walls. 
The air is thick with the scent of old parchment and a hint of something else—incense or some other magical essence. 
Dust floats in the light beams, creating a surreal, almost ethereal atmosphere.
        """,
        """
At first glance, the tower seems abandoned. Cobwebs drape from the ceiling, and broken furniture lies scattered across the stone floor. 
The walls are lined with shelves containing ancient books and alchemical equipment, hinting at the tower's former purpose. 
Despite the apparent emptiness, you can't shake the feeling that you're being watched.
        """,
        """
You venture deeper into the tower, the echoes of your footsteps amplifying in the empty halls. 
As you turn a corner, a flickering light catches your eye. 
A single candle burns at the far end of a long corridor, its flame casting eerie shadows on the walls. 
You approach cautiously, your senses alert for any sign of movement.
        """,
        """
Just as you reach the candle, a figure steps from the shadows, cloaked in dark robes. 
The wizard, his face obscured by a hood, raises his hand, and the candle's flame flares brightly, illuminating the room. 
His voice, low and resonant, fills the corridor.
        """
        """
"Who dares enter my tower?" he asks, his tone laced with menace. "Have you come to seek knowledge, or do you bring trouble?"
You stand your ground, meeting the wizard's gaze. His eyes are a piercing blue, filled with a mix of curiosity and suspicion. 
The atmosphere crackles with latent magic, and you sense that this wizard is no ordinary conjurer. 
He could be an ally—or a formidable adversary.
        """
        """
As you consider your next move, the wizard continues to study you, his fingers idly tracing symbols in the air. 
Whatever lies ahead in this tower, you'll need to navigate carefully. 
The wizard holds the key to something that may help you in your quest to slay the dragon, 
but gaining his trust—or defeating him—will require all your wits and skill.
        """
        """
The wizard's eyes narrow as he studies you, his fingers still tracing arcane symbols in the air.
"You seek the dragon," he says, his voice a low murmur. "A noble quest, but one fraught with peril. 
I can aid you in your journey, but first, you must prove your worth. Face me in battle, and if you emerge victorious, 
I will share my knowledge with you."
        """
        """
The air grows tense as you prepare for the wizard's challenge. 
His robe sways as if caught by an invisible wind, and the symbols he traces start to glow with a faint blue light. 
He moves with an almost otherworldly grace, each step deliberate, each gesture precise. 
You can sense the immense power at his command, the very essence of magic that could either help or hinder you in your quest to slay the dragon.
        """
        """
You take a defensive stance, ready for whatever spells or incantations he might unleash. 
The wizard watches you with a mix of curiosity and cunning, as if gauging your potential. 
His challenge is clear: defeat him, and gain his knowledge; fail, and your journey may end here, in the shadowy depths of this tower.
        """
        """
As the air crackles with magical energy, you know that this battle will test not only your combat skills but also your ability to adapt to the unpredictable forces of magic. 
The wizard's power is formidable, but so is your resolve. With a deep breath, you brace yourself for the duel ahead, 
knowing that victory will bring you one step closer to your ultimate goal—the dragon's demise.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()

def wizardOutro():
    lore = [
        f"""
The wizard collapses to his knees, his robe billowing as the magical energy around him dissipates. The glowing symbols fade, and the tower falls into a quiet stillness, the echoes of your battle lingering in the air. He raises his head, his expression a mix of defeat and acceptance, as if the outcome was inevitable.
        """,
        """
"You are strong," he says, his voice calm but tinged with a hint of sadness. "Stronger than I expected. It seems I underestimated you."
The wizard slowly rises, his gaze fixed on you with a newfound respect. The arcane symbols traced in the air vanish entirely, 
replaced by the steady glow of the candlelight. He walks toward you, his steps deliberate but without aggression.
        """,
        """
"For years, I believed that I was the one destined to fulfill the prophecy," he continues, his words slow and measured. 
"The prophecy of the one who would defeat the dragon and restore balance to the realm. 
I trained, studied, and prepared for the day I would face the beast, but as time went on, I realized that I was not the one. 
My magic was not strong enough, my resolve not unbreakable."
        """,
        """
The wizard pauses, his eyes studying you as if trying to understand what makes you different. 
He sighs, a breath that seems to carry the weight of years of disappointment.

"I thought all was lost," he admits. "Until you came along. You have the strength and the courage that I lacked. 
You defeated me, proving your worthiness to face the dragon. Perhaps you are the one the prophecy spoke of—the one who will bring peace to the land."
        """,
        """
He gestures toward a large, ornate chest against the wall, its surface carved with intricate runes. 
"I will help you on your journey," he says. "Within this chest is something that may aid you in your quest. 
Take it, and use it wisely. I will also share my knowledge with you, guiding you on the path to the dragon's lair."
        """,
        """
The wizard's demeanor has changed, from adversary to reluctant ally. 
You have proven yourself in battle, and now he sees you as the hope he thought was lost. 
With his guidance and the artifact from the chest, your journey continues, leading you ever closer to the ultimate confrontation with the dragon.
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()


def giantIntro():
	lore = [
		f"""
This will be the giant intro
		"""
	]
	for text in lore:
		print_with_delay(text, TEXT_SPEED)
		input("\nPress enter to continue...")
		clear_console()

def giantOutro():
	lore = [
		f"""
This will be the giant outro
		"""
	]
     
def minotaurIntro():
	lore = [
		f"""
This will be the minotaur intro
		"""
	]
	for text in lore:
		print_with_delay(text, TEXT_SPEED)
		input("\nPress enter to continue...")
		clear_console()

def minotaurOutro():
    lore = [
        f"""
This will be the minotaur outro
        """
    ]
    for text in lore:
        print_with_delay(text, TEXT_SPEED)
        input("\nPress enter to continue...")
        clear_console()


def dragonIntro():
	lore = [
		f"""
This will be the dragon intro
		"""
	]
def dragonOutro():
	lore = [
		f"""
This will be the dragon outro
		"""
	]
	for text in lore:
		print_with_delay(text, TEXT_SPEED)
		input("\nPress enter to continue...")
		clear_console()


def end_game():
	lore = [
		f"""
This will be the end game lore
		"""
	]
	for text in lore:
		print_with_delay(text, TEXT_SPEED)
		input("\nPress enter to continue...")
		clear_console()