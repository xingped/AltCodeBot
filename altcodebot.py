import regex
import praw
import sys
import time
import shelve

session = ''
ignusr_store = ''
ignsub_store = ''

def quick_url(comment):
	"""Return the URL for the comment without fetching its submission."""
	def to_id(fullname):
		return fullname.split('_', 1)[1]
	return ('http://www.reddit.com/r/{0}/comments/{1}/_/{2}?context=3'.format(comment.subreddit.display_name, to_id(comment.link_id), comment.id))

def commands():
	global ignusr_store, ignsub_store
	for msg in session.get_unread(limit=None):
		match = regex.search("!ignore me", msg.body.lower())
		if match:
			ignusr_store[msg.author.name.lower()] = 1
			print('\nIgnoring User:', msg.author.name.lower())
			msg.reply('User {0} will be ignored from now on.'.format(msg.author.name))
		
		match = regex.search("!ignore sub", msg.body.lower())
		if match and comment.author in r.get_moderators(comment.subreddit):
			ignsub_store[msg.subreddit.lower()] = 1
			print('\nIgnoring Subreddit:', msg.subreddit.lower())
			msg.reply('Subreddit {0} will be ignored from now on.'.format(msg.subreddit))
		
		msg.mark_as_read()
		
def main():
	# Create Unicode Character Array
	unidict = {
		'\u263a': 'ALT+1, "White Smiling Face"',
		'\u263b': 'ALT+2, "Black Smiling Face"',
		'\u2665': 'ALT+3, "Black Heart Suit"',
		'\u2666': 'ALT+4, "Black Diamond Suit"',
		'\u2663': 'ALT+5, "Black Club Suit"',
		'\u2660': 'ALT+6, "Black Spade Suit"',
		'\u25d8': 'ALT+8, "Inverse Bullet"',
		'\u25cb': 'ALT+9, "White Circle"',
		'\u25d9': 'ALT+10, "Inverse White Circle"',
		'\u2642': 'ALT+11, "Male Sign"',
		'\u2640': 'ALT+12, "Female Sign"',
		'\u266a': 'ALT+13, "Eighth Note"',
		'\u266b': 'ALT+14, "Beamed Eighth Notes"',
		'\u263c': 'ALT+15, "White Sun With Rays"',
		'\u25ba': 'ALT+16, "Black Right-Pointing Pointer"',
		'\u25c4': 'ALT+17, "Black Left-Pointing Pointer"',
		'\u2195': 'ALT+18, "Up Down Arrow"',
		'\u203c': 'ALT+19, "Double Exclamation Mark"',
		'\u00b6': 'ALT+20, "Pilcrow Sign"',
		'\u00a7': 'ALT+21, "Section Sign"',
		'\u25ac': 'ALT+22, "Black Rectangle"',
		'\u21a8': 'ALT+23, "Up Down Arrow With Base"',
		'\u2191': 'ALT+24, "Upwards Arrow"',
		'\u2193': 'ALT+25, "Downwards Arrow"',
		'\u2192': 'ALT+26, "Rightwards Arrow"',
		'\u2190': 'ALT+27, "Leftwards Arrow"',
		'\u221f': 'ALT+28, "Right Angle"',
		'\u2194': 'ALT+29, "Left Right Arrow"',
		'\u25b2': 'ALT+30, "Black Up-Pointing Triangle"',
		'\u25bc': 'ALT+31, "Black Down-Pointing Triangle"',
		'\u2302': 'ALT+127, "House"',
		#'\u00aa': 'ALT+166, "Feminine Ordinal Indicator"',
		#'\u00ba': 'ALT+167, "Masculine Ordinal Indicator"',
		#'\u2310': 'ALT+169, "Reversed Not Sign"',
		#'\u00ac': 'ALT+170, "Not Sign"',
		#'\u00bd': 'ALT+171, "Vulgar Fraction One Half"',
		#'\u00bc': 'ALT+172, "Vulgar Fraction One Quarter"',
		#'\u00ab': 'ALT+174, "Left-Pointing Double Angle Quotation Mark"',
		#'\u00bb': 'ALT+175, "Right-Pointing Double Angle Quotation Mark"',
		#'\u2591': 'ALT+176, "Light Shade"',
		#'\u2592': 'ALT+177, "Medium Shade"',
		#'\u2593': 'ALT+178, "Dark Shade"',
		#'\u2502': 'ALT+179, "Box Drawings Light Vertical"',
		#'\u2524': 'ALT+180, "Box Drawings Light Vertical And Left"',
		#'\u2561': 'ALT+181, "Box Drawings Vertical Single And Left Double"',
		#'\u2562': 'ALT+182, "Box Drawings Vertical Double And Left Single"',
		#'\u2556': 'ALT+183, "Box Drawings Down Double And Left Single"',
		#'\u2555': 'ALT+184, "Box Drawings Down Single And Left Double"',
		#'\u2563': 'ALT+185, "Box Drawings Double Vertical And Left"',
		#'\u2551': 'ALT+186, "Box Drawings Double Vertical"',
		#'\u2557': 'ALT+187, "Box Drawings Double Down And Left"',
		#'\u255d': 'ALT+188, "Box Drawings Double Up And Left"',
		#'\u255c': 'ALT+189, "Box Drawings Up Double And Left Single"',
		#'\u255b': 'ALT+190, "Box Drawings Up Single And Left Double"',
		#'\u2510': 'ALT+191, "Box Drawings Light Down And Left"',
		#'\u2514': 'ALT+192, "Box Drawings Light Up And Right"',
		#'\u2534': 'ALT+193, "Box Drawings Light Up And Horizontal"',
		#'\u252c': 'ALT+194, "Box Drawings Light Down And Horizontal"',
		#'\u251c': 'ALT+195, "Box Drawings Light Vertical And Right"',
		#'\u2500': 'ALT+196, "Box Drawings Light Horizontal"',
		#'\u253C': 'ALT+197, "Box Drawings Light Vertical And Horizontal"',
		#'\u255e': 'ALT+198, "Box Drawings Vertical Single And Right Double"',
		#'\u255f': 'ALT+199, "Box Drawings Vertical Double And Right Single"',
		#'\u255a': 'ALT+200, "Box Drawings Double Up And Right"',
		#'\u2554': 'ALT+201, "Box Drawings Double Down And Right"',
		#'\u2569': 'ALT+202, "Box Drawings Double Up And Horizontal"',
		#'\u2566': 'ALT+203, "Box Drawings Double Down And Horizontal"',
		#'\u2560': 'ALT+204, "Box Drawings Double Vertical And Right"',
		#'\u2550': 'ALT+205, "Box Drawings Double Horizontal"',
		#'\u256c': 'ALT+206, "Box Drawings Double Vertical And Horizontal"',
		#'\u2567': 'ALT+207, "Box Drawings Up Single And Horizontal Double"',
		#'\u2568': 'ALT+208, "Box Drawings Up Double And Horizontal Single"',
		#'\u2564': 'ALT+209, "Box Drawings Down Single And Horizontal Double"',
		#'\u2565': 'ALT+210, "Box Drawings Down Double And Horizontal Single"',
		#'\u2559': 'ALT+211, "Box Drawings Up Double And Right Single"',
		#'\u2558': 'ALT+212, "Box Drawings Up Single And Right Double"',
		#'\u2552': 'ALT+213, "Box Drawings Down Single And Right Double"',
		#'\u2553': 'ALT+214, "Box Drawings Down Double And Right Single"',
		#'\u256b': 'ALT+215, "Box Drawings Vertical Double And Horizontal Single"',
		#'\u256a': 'ALT+216, "Box Drawings Vertical Single And Horizontal Double"',
		#'\u2518': 'ALT+217, "Box Drawings Light Up And Left"',
		#'\u250c': 'ALT+218, "Box Drawings Light Down And Right"',
		#'\u2588': 'ALT+219, "Full Block"',
		#'\u2584': 'ALT+220, "Lower Half Block"',
		#'\u258c': 'ALT+221, "Left Half Block"',
		#'\u2590': 'ALT+222, "Right Half Block"',
		#'\u2580': 'ALT+223, "Upper Half Block"',
		#'\u03b1': 'ALT+224, "Greek Small Letter Alpha"',
		#'\u0393': 'ALT+226, "Greek Capital Letter Gamma"',
		#'\u03c0': 'ALT+227, "Greek Small Letter Pi"',
		#'\u03a3': 'ALT+228, "Greek Capital Letter Sigma"',
		#'\u03c3': 'ALT+229, "Greek Small Letter Sigma"',
		#'\u00b5': 'ALT+230, "Micro Sign"',
		#'\u03c4': 'ALT+231, "Greek Small Letter Tau"',
		#'\u03a6': 'ALT+232, "Greek Capital Letter Phi"',
		#'\u0398': 'ALT+233, "Greek Capital Letter Theta"',
		#'\u03a9': 'ALT+234, "Greek Capital Letter Omega"',
		#'\u03b4': 'ALT+235, "Greek Small Letter Delta"',
		'\u221e': 'ALT+236, "Infinity"',
		#'\u03c6': 'ALT+237, "Greek Small Letter Phi"',
		#'\u03b5': 'ALT+238, "Greek Small Letter Epsilon"',
		'\u2229': 'ALT+239, "Intersection"',
		'\u2261': 'ALT+240, "Identical To"',
		'\u00b1': 'ALT+241, "Plus-Minus Sign"',
		'\u2265': 'ALT+242, "Greater-Than Or Equal To"',
		'\u2264': 'ALT+243, "Less-Than Or Equal To"',
		'\u2320': 'ALT+244, "Top Half Integral"',
		'\u2321': 'ALT+245, "Bottom Half Integral"',
		'\u00f7': 'ALT+246, "Division Sign"',
		'\u2248': 'ALT+247, "Almost Equal To"',
		#'\u00b0': 'ALT+248, "Degree Sign"',
		#'\u2219': 'ALT+249, "Bullet Operator"',
		#'\u00b7': 'ALT+250, "Middle Dot"',
		'\u221a': 'ALT+251, "Square Root"',
		#'\u207f': 'ALT+252, "Superscript Latin Small Letter N"',
		#'\u00b2': 'ALT+253, "Superscript Two"',
		#'\u25a0': 'ALT+254, "Black Square"'
	}
	
	# Open shelves and get ignore sets
	global ignusr_store, ignsub_store
	ignusr_store = shelve.open('ignore_users.db', writeback=True)
	ignsub_store = shelve.open('ignore_subs.db', writeback=True)
	ignusr_list = list(ignusr_store.keys())
	ignsub_list = list(ignsub_store.keys())
	print('Ignoring users: ', ignusr_list)
	print('Ignoring subs: ', ignsub_list)
	
	# Start session
	global session
	session = praw.Reddit('AltCodeBot v1.0 by /u/xingped')
	cred_store = shelve.open('credentials.db')
	session.login(cred_store['user'], cred_store['password'])
	
	# Use 'all' subreddit
	subreddit = 'botplayground'
	
	# Already viewed comments
	comments_done = []
	
	try:
		for comment in praw.helpers.comment_stream(session, subreddit, verbosity=0):
			if comment.author and comment.author.name.lower() in ignusr_list:
				continue
			
			if comment.subreddit in ignsub_list:
				continue
			
			if comment.id in comments_done:
				continue
			
			replytext = "Hello, it looks like you used some special characters that can be typed with Alt Codes.\n\nHere's the codes for those characters:\n\n"
			comment_reply = 0
			
			for k,v in unidict.items():
				match = regex.search(k, comment.body, flags=regex.UNICODE)
				if match:
					if comment_reply == 0:
						url = quick_url(comment)
						print('{0}: {1}'.format(comment.id, url))
						comment_reply = 1
					print('* {0} : {1}'.format(k, v))
					replytext += '* {0} : {1}\n'.format(k, v)
			
			replytext += "\n\nPlease let me know if you like me, hate me, or think I've made a mistake."
			replytext += "\n\n**Commands:** '!ignore me' (User), '!ignore sub' (Mods)"
			
			comments_done.append(comment.id)
			
			commands()
			
			if comment_reply == 1:
				comment.reply(replytext)
				print("\n\nSleeping...")
				time.sleep(1*60)
				print("And I'm back!\n")
				
	except KeyboardInterrupt:
		cred_store.close()
		ignusr_store.close()
		ignsub_store.close()
		sys.stderr.write('\n')
		print('Goodbye!\n')
		
if __name__ == '__main__':
	main()