import os, time, sys, threading
from utils import print_lore
from global_vars import stop_thread

TEXT_SPEED = 0.02  # Adjust this value to change the speed of the text

def introLore(hero_name):
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
    print_lore(lore)

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
    print_lore(lore)


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
    print_lore(lore)

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
    print_lore(lore)

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
    print_lore(lore)


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
    print_lore(lore)

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
    print_lore(lore)


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
        """,
        """
"Who dares enter my tower?" he asks, his tone laced with menace. "Have you come to seek knowledge, or do you bring trouble?"
You stand your ground, meeting the wizard's gaze. His eyes are a piercing blue, filled with a mix of curiosity and suspicion. 
The atmosphere crackles with latent magic, and you sense that this wizard is no ordinary conjurer. 
He could be an ally—or a formidable adversary.
        """,
        """
As you consider your next move, the wizard continues to study you, his fingers idly tracing symbols in the air. 
Whatever lies ahead in this tower, you'll need to navigate carefully. 
The wizard holds the key to something that may help you in your quest to slay the dragon, 
but gaining his trust—or defeating him—will require all your wits and skill.
        """,
        """
The wizard's eyes narrow as he studies you, his fingers still tracing arcane symbols in the air.
"You seek the dragon," he says, his voice a low murmur. "A noble quest, but one fraught with peril. 
I can aid you in your journey, but first, you must prove your worth. Face me in battle, and if you emerge victorious, 
I will share my knowledge with you."
        """,
        """
The air grows tense as you prepare for the wizard's challenge. 
His robe sways as if caught by an invisible wind, and the symbols he traces start to glow with a faint blue light. 
He moves with an almost otherworldly grace, each step deliberate, each gesture precise. 
You can sense the immense power at his command, the very essence of magic that could either help or hinder you in your quest to slay the dragon.
        """,
        """
You take a defensive stance, ready for whatever spells or incantations he might unleash. 
The wizard watches you with a mix of curiosity and cunning, as if gauging your potential. 
His challenge is clear: defeat him, and gain his knowledge; fail, and your journey may end here, in the shadowy depths of this tower.
        """,
        """
As the air crackles with magical energy, you know that this battle will test not only your combat skills but also your ability to adapt to the unpredictable forces of magic. 
The wizard's power is formidable, but so is your resolve. With a deep breath, you brace yourself for the duel ahead, 
knowing that victory will bring you one step closer to your ultimate goal—the dragon's demise.
        """
    ]
    print_lore(lore)

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
    print_lore(lore)

def giantIntro():
    lore = [
		f"""
As you grasp the magic staff, a surge of energy courses through you, vibrant and powerful. 
The arcane symbols etched into the wood pulse with a rhythmic light, and you feel a new reservoir of power opening within you.
This is mana—the essence of magic that allows you to unleash devastating attacks with a single thought. 
The staff hums in your grip, resonating with your newfound energy.
		""",
		"""
With this potent weapon, you set out from the wizard's tower, the path leading toward the rugged mountains where your next challenge awaits. 
The terrain becomes rougher, the ground littered with rocks and sparse vegetation. 
The sky overhead is overcast, casting a muted gray light over the landscape. 
It’s a fitting backdrop for what you know is coming.
		""",
		"""
As you ascend a rocky slope, a shadow falls across your path. 
You look up to see a massive figure standing at the peak of the hill—a giant, towering and menacing. 
Its skin is like rough stone, and its muscles ripple with every move. 
The giant wields an enormous club, its wood splintered from countless battles. 
When it moves, the ground trembles, sending small rocks rolling down the hillside.
		""",
		"""
The giant’s voice is a low rumble, deep and guttural. It calls out to you, its words unintelligible but filled with menace. 
It takes a step forward, shaking the earth beneath your feet. This is no ordinary giant; 
it's a guardian of the mountain pass, a fearsome sentinel that has crushed countless intruders. 
And now it has set its sights on you.
		""",
		"""
With the magic staff in hand, you feel a surge of confidence. 
The mana flowing through you is potent, each pulse an affirmation of your new power. 
You know that you must defeat this giant to continue your journey and that the powerful attack granted by the staff could be the key to victory.
		"""
	]
    print_lore(lore)

def giantOutro():
    lore = [
		f"""
With a burst of mana, you channel the staff's energy into a devastating attack. 
The pulse of magic strikes the giant with overwhelming force, sending it reeling backward. 
It stumbles, its massive form crashing into the hillside with a tremendous thud. 
Dust and debris billow into the air as the giant collapses, defeated. 
The ground is still, the echoes of battle fading into the wind.
		""",
		"""
You stand over the fallen giant, your grip tightening on the magic staff. 
The path ahead is clear, but you know that this victory is just a step on your journey toward the dragon's lair. 
Beyond the rocky landscape, a structure comes into view—a labyrinth, ancient and foreboding. 
Its stone walls rise high, twisting and turning in complex patterns. 
This is the Minotaur's Labyrinth, a place of legend where many have entered but few have emerged.
		""",
		"""
As you approach the labyrinth's entrance, you sense an ominous presence. 
The air grows colder, and the light dims as the walls of the maze seem to close in. 
The Minotaur is said to guard the heart of the labyrinth, a creature born of myth and fury. 
It is a formidable beast, part man, part bull, with immense strength and a brutal cunning that makes it a deadly adversary.
		""",
		"""
Beyond the labyrinth lies the dragon's lair, the final destination of your journey. 
But first, you must navigate the twisting corridors, avoid the traps and pitfalls, and confront the Minotaur that guards the maze. 
Each step into the labyrinth brings you closer to the dragon, but it also brings new dangers and challenges that will test your skill and resolve.
		""",
		"""
You take a deep breath, the scent of moss and stone filling your lungs. 
The labyrinth's entrance stands before you, its dark passage beckoning. 
With the magic staff in hand, you know you have the power to overcome the challenges ahead, but the path will not be easy.
The dragon awaits, but first, you must face the Minotaur and find your way through the labyrinth's maze of stone and shadow.
		"""
	]
    print_lore(lore)

def minotaurIntro():
    lore = [
		f"""
You step into the labyrinth, the stone walls closing behind you, casting the corridor into shadowy gloom. 
The air is damp and cool, with the faint scent of mildew and earth. You move cautiously, each footstep echoing through the winding passageways. 
The labyrinth is a maze of twists and turns, with high walls that obscure your view of what lies ahead. 
You know that somewhere within this maze lurks the Minotaur, the guardian of the labyrinth.
		""",
		"""
As you navigate through the labyrinth, you come across ancient carvings on the walls depicting past adventurers and their struggles against the Minotaur. 
These faded images serve as a reminder of the dangers that lie ahead and the fate of those who came before you. 
The silence in the labyrinth is unnerving, broken only by the distant drip of water and the occasional gust of wind that sweeps through the corridors.
		""",
		"""
Turning a corner, you suddenly hear the sound of heavy breathing, deep and labored, followed by the faint scraping of hooves against stone. 
You freeze, your senses on high alert, as the sound grows louder. The Minotaur is close. 
The guardian of the labyrinth is massive, a beast with the body of a man and the head of a bull. 
Its horns are long and sharp, capable of impaling anyone who dares to cross its path.
		""",
		"""
The Minotaur emerges from the shadows, its eyes glowing with a feral intensity. It lets out a low, rumbling growl as it catches sight of you. 
Its muscles ripple with each movement, and the ground seems to vibrate as it stomps toward you. 
The Minotaur carries a massive axe, its blade chipped but deadly, a weapon that has seen countless battles.
		""",
		"""
You grip your magic staff, feeling the surge of mana flowing through it. 
The Minotaur's roar reverberates through the labyrinth, echoing off the walls and filling the air with its raw power.
This is the guardian you must defeat to reach the dragon's lair. There is no turning back now.
		""",
		"""
With a deep breath, you brace yourself for the battle to come. The Minotaur charges, its horns aimed at you, its hooves pounding against the stone floor. 
You know this encounter will be a test of both strength and strategy, and your only way forward is through the beast that stands in your path.
		"""
	]
    print_lore(lore)

def minotaurOutro():
    lore = [
		f"""
With a final strike, the Minotaur staggers and collapses to the ground, 
the thunderous sound of its fall echoing through the labyrinth. 
Its massive form is still, the air heavy with the scent of battle and sweat. 
You stand over the beast, your heart racing, knowing that this victory has taken you one step closer to your ultimate goal.
		""",
		"""
You sever the Minotaur's head, a gruesome trophy that marks your triumph over the labyrinth's guardian. 
Holding it high, you feel a surge of pride and resolve. 
It’s a symbol of your strength and determination—proof that nothing will stand in your way as you pursue the dragon.
		""",
		"""
Beside the fallen Minotaur, you find its battle axe, a mighty weapon that reflects the labyrinth's eerie light. 
The axe is massive, with a broad blade and a sturdy handle, showing signs of wear from countless battles. 
You pick it up, feeling its weight and balance, knowing it will serve you well in the challenges to come.
		""",
		"""
With the Minotaur defeated, you navigate the remaining twists and turns of the labyrinth, using your newfound trophy as a guide. 
The corridors eventually lead to an exit, where you push open a heavy stone door to find yourself in the open air once more.
		""",
		"""
The sun is setting, casting a warm glow over the landscape. 
In the distance, you see the dragon's lair—a dark, foreboding cave carved into the side of a mountain. 
The air around it is filled with smoke and the faint scent of brimstone, a clear sign of the dragon's presence. 
The cave mouth is enormous, framed by jagged rocks and surrounded by scorch marks. It's a place of legend, a place that has claimed the lives of many would-be heroes.
		""",
		"""
As you stand at the edge of the labyrinth, the dragon's lair looming in the distance, you feel a mix of anticipation and apprehension. 
The journey has brought you through dangerous forests, over treacherous bridges, and into the heart of a deadly labyrinth. 
But the ultimate challenge still lies ahead.
		""",
		"""
With the Minotaur's head as your trophy and its battle axe in hand, you take a deep breath and step forward, ready to face the dragon and fulfill the prophecy. 
The lair beckons, and you are determined to end the dragon's reign once and for all.
		"""
	]
    print_lore(lore)

def dragonIntro():
    lore = [
		f"""
The dragon's lair looms large as you approach, its massive entrance like the gaping maw of some ancient beast. 
Jagged rock formations rise around it, the walls darkened by centuries of smoke and fire. 
As you step into the cave, the air grows warmer, heavy with the scent of sulfur and ash. 
Echoes of distant roars and the faint rustling of scales reverberate off the walls, 
a reminder that this is the domain of a creature of immense power.


		""",
		"""
Equipped with the magic staff and the Minotaur's battle axe, you enter the lair with cautious confidence. 
Each step into the cavern feels like a step into history, the bones of past adventurers strewn across the ground, 
their weapons and armor rusted and broken. The flickering light from the torches you carry casts eerie shadows on the stone,
creating the illusion of movement in every corner.


		""",
		"""
The lair is vast, with high ceilings and wide chambers, but it's the inner sanctum you seek—the dragon's throne room, 
where it guards its hoard and rests between flights. 
The path is winding and treacherous, with narrow ledges and steep drops. 
You navigate these dangers, mindful of traps and hidden passages, knowing that any misstep could be fatal.
		""",
		"""
As you venture deeper into the lair, the ambient heat grows more intense. 
The walls are scorched, and molten rock flows in rivulets along the cavern's edges, 
a constant reminder of the dragon's fiery breath. The sound of distant growls becomes more pronounced, 
growing louder with each step. You know that the dragon is close, 
and that this battle will be the ultimate test of your skill and courage.
		""",
		"""
Finally, you reach the heart of the lair—the dragon's throne room. 
It's a vast, circular chamber with a high, vaulted ceiling. 
In the center lies the dragon, its massive body coiled around a mountain of treasure—gold, jewels, and relics of past kingdoms. 
Its scales shimmer in the dim light, each one as dark as obsidian and as hard as steel. 
The dragon's eyes open slowly, revealing a deep, smoldering red, like the core of a volcano. 
It rises, stretching its wings, the sheer size of its body filling the chamber with an ominous presence.
		""",
		"""
The dragon roars, a sound that shakes the very walls of the lair, sending ripples through the molten rock below. 
It glares at you, its eyes filled with ancient malice and an understanding that you are here to end its reign. 
You grip the magic staff and the Minotaur's battle axe, ready for the fight of your life.
		""",
		"""
This is the final battle. The dragon, a symbol of terror and destruction, stands between you and your destiny. 
With a deep breath, you steel yourself for the conflict, knowing that this encounter will determine the fate of the realm. 
The dragon lunges, its wings spreading wide, and you step forward, prepared to face your ultimate foe.
		"""
	]
    print_lore(lore)

def dragonOutro():
    lore = [
		f"""

With a mighty swing of the Minotaur's battle axe, you strike the final blow. 
The dragon reels, its roar turning into a low, agonized rumble as it collapses to the ground. 
The sound reverberates through the cavern, mingling with the crash of falling rocks and the hiss of steam from molten lava. 
The dragon's massive body lies still, its wings spread wide, a monument to its defeat.
		""",
		"""
The chamber falls silent, the echoes of battle slowly fading into the depths of the lair. 
You stand over the dragon's body, the heat of its scales still radiating through the chamber. 
The journey has been long and fraught with peril, but you have overcome each challenge, each foe, to reach this point. 
You have slain the dragon, fulfilling the prophecy and bringing hope back to the realm.
		""",
		"""
As you survey the scene, the dragon's hoard stretches before you, a testament to the beast's long reign of terror. 
Gold coins, jewels, and ancient artifacts glimmer in the dim light, but your victory is far more valuable than any treasure.
You have ended a legacy of fear and destruction, and the realm is now free to rebuild and thrive.
		""",
		"""
You take a moment to catch your breath, the adrenaline of battle slowly fading. T
he magic staff and the Minotaur's battle axe are heavy in your hands, but they have served you well. 
You look around the chamber, seeing the remnants of past battles, the bones of those who came before you. 
Their sacrifices were not in vain. You have accomplished what they could not—you have slain the dragon and saved the realm.
		""",
		"""
As you leave the lair, the sky outside is painted with the colors of dawn. 
The first light of morning breaks over the horizon, casting a golden glow across the landscape. 
You make your way back through the forest, the once-ominous shadows now retreating in the face of the rising sun. 
The realm awakens to a new day, a day free from the fear of the dragon's wrath.
		""",
		"""
Word of your victory spreads quickly, and by the time you reach the nearest village, a crowd has gathered to greet you. 
Their cheers and applause fill the air, a chorus of gratitude for the hero who has saved them. 
You are hailed as the champion of the realm, the one who defeated the dragon and brought peace to the land.
		""",
		"""
As you stand before the cheering crowd, the weight of your journey falls away, replaced by a sense of accomplishment and pride. 
You have faced unimaginable challenges, battled fierce foes, and emerged victorious. 
The realm is forever changed because of your bravery and determination. 
You are a hero, a legend, and your name will be remembered for generations to come.
		"""
	]
    print_lore(lore)

def end_game(hero_name):
    lore = [
        f"""
And so, the hero known as {hero_name} emerged from the dragon's lair, victorious and revered.
The realm was forever changed by their bravery and resolve, and the people hailed them as a savior.
        """,
        """
The dragon's reign of terror was ended, its dark shadow lifted from the land.
The villages prospered, the forests grew green once more, and the mountains echoed with the songs of celebration.
        """,
        """
{hero_name} had fulfilled the prophecy, bringing peace and hope back to the realm.
Their journey was long and perilous, but they had faced each challenge with courage and strength.
        """,
        """
The hero's name became a legend, a tale told around hearthfires and in the halls of kings.
Their deeds were immortalized in song and story, a testament to the power of one brave soul.
        """,
        """
And though the hero's journey had come to an end, their legacy lived on in the hearts of all who knew their name.
{hero_name} had saved the realm, and their story would be told for generations to come.
        """
    ]
    print_lore(lore)