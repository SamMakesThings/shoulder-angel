import weave

task_analyzer_dataset = weave.Dataset(
    name="shoulder-angel-task-analyzer-dataset-2",
    rows=weave.Table(
        [
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Finish Python project for presentation.",
                "recent_ocr": "Reddit /r/memes funny memes jokes family guy  \n            Top posts: 1. When you finally beat that boss 2. Me trying to adult 3. Wholesome grandma moment 4. That feeling when you find the perfect gif 5. Video game logic be like\n            Comments: 'This is too relatable' 'I can't stop laughing' 'Take my upvote' 'Someone give this person gold'\n            Subreddit rules: 1. All posts must be memes 2. No reposts 3. Be nice to others",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Reddit /r/memes funny memes jokes family guy  \n            Top posts: 1. When you finally beat that boss 2. Me trying to adult 3. Wholesome grandma moment 4. That feeling when you find the perfect gif 5. Video game logic be like\n            Comments: 'This is too relatable' 'I can't stop laughing' 'Take my upvote' 'Someone give this person gold'\n            Subreddit rules: 1. All posts must be memes 2. No reposts 3. Be nice to others"
                    },
                    {
                        "role": "assistant",
                        "content": "Hi, Sam. How's it going? I noticed currently exploring your MacBook Pro settings, but I'm not clear on how this activity aligns with your current goals. Can you help me understand what you're trying to accomplish?"
                    },
                    {
                        "role": "user",
                        "content": "I'm trying to debug a problem."
                    },
                    {
                        "role": "assistant",
                        "content": "Debugging can be a challenge."
                    }
                ],
                "target_output": "False"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Finish Python project for presentation.",
                "recent_ocr": "Python 3.9.5 Documentation\n\nPython HOWTOs\nPython HOWTOs are documents that cover a single, specific topic, and attempt to cover it fairly completely. Modeled on the Linux Documentation Project's HOWTO collection, this collection is an effort to foster documentation that's more detailed than the Python Library Reference.\n\nCurrently, the HOWTOs are:\n\nArgparse Tutorial\nAuthenticating to GitHub using SSH\nCoding Style\nCursor Objects\nDescriptor HowTo Guide\nFunctional Programming HOWTO\nLogging HOWTO\nLogging Cookbook\nRegular Expression HOWTO\nSocket Programming HOWTO\nSorting HOW TO\nUnicode HOWTO\n\nIndices and tables\nIndex\nModule Index\nSearch Page",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Python 3.9.5 Documentation\n\nPython HOWTOs\nPython HOWTOs are documents that cover a single, specific topic, and attempt to cover it fairly completely. Modeled on the Linux Documentation Project's HOWTO collection, this collection is an effort to foster documentation that's more detailed than the Python Library Reference.\n\nCurrently, the HOWTOs are:\n\nArgparse Tutorial\nAuthenticating to GitHub using SSH\nCoding Style\nCursor Objects\nDescriptor HowTo Guide\nFunctional Programming HOWTO\nLogging HOWTO\nLogging Cookbook\nRegular Expression HOWTO\nSocket Programming HOWTO\nSorting HOW TO\nUnicode HOWTO\n\nIndices and tables\nIndex\nModule Index\nSearch Page"
                    },
                    {
                        "role": "assistant",
                        "content": "Hi, Sam. How's it going? I noticed currently exploring your MacBook Pro settings, but I'm not clear on how this activity aligns with your current goals. Can you help me understand what you're trying to accomplish?"
                    },
                    {
                        "role": "user",
                        "content": "I'm trying to debug a problem."
                    },
                    {
                        "role": "assistant",
                        "content": "Debugging can be a challenge."
                    }
                ],
                "target_output": "True"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Learn React for web development project.",
                "recent_ocr": "React Documentation\n\nMain Concepts\n1. Hello World\n2. Introducing JSX\n3. Rendering Elements\n4. Components and Props\n5. State and Lifecycle\n6. Handling Events\n7. Conditional Rendering\n8. Lists and Keys\n9. Forms\n10. Lifting State Up\n11. Composition vs Inheritance\n12. Thinking In React\n\nAdvanced Guides\n• Accessibility\n• Code-Splitting\n• Context\n• Error Boundaries\n• Forwarding Refs\n• Fragments\n• Higher-Order Components\n• Integrating with Other Libraries\n• JSX In Depth\n• Optimizing Performance\n• Portals\n• Profiler\n• React Without ES6\n• React Without JSX\n• Reconciliation\n• Refs and the DOM\n• Render Props\n• Static Type Checking\n• Strict Mode\n• Typechecking With PropTypes\n• Uncontrolled Components\n• Web Components",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: React Documentation\n\nMain Concepts\n1. Hello World\n2. Introducing JSX\n3. Rendering Elements\n4. Components and Props\n5. State and Lifecycle\n6. Handling Events\n7. Conditional Rendering\n8. Lists and Keys\n9. Forms\n10. Lifting State Up\n11. Composition vs Inheritance\n12. Thinking In React\n\nAdvanced Guides\n• Accessibility\n• Code-Splitting\n• Context\n• Error Boundaries\n• Forwarding Refs\n• Fragments\n• Higher-Order Components\n• Integrating with Other Libraries\n• JSX In Depth\n• Optimizing Performance\n• Portals\n• Profiler\n• React Without ES6\n• React Without JSX\n• Reconciliation\n• Refs and the DOM\n• Render Props\n• Static Type Checking\n• Strict Mode\n• Typechecking With PropTypes\n• Uncontrolled Components\n• Web Components"
                    },
                    {
                        "role": "assistant",
                        "content": "Hi, Sam. How's it going? I noticed currently exploring your MacBook Pro settings, but I'm not clear on how this activity aligns with your current goals. Can you help me understand what you're trying to accomplish?"
                    },
                    {
                        "role": "user",
                        "content": "I'm trying to debug a problem."
                    },
                    {
                        "role": "assistant",
                        "content": "Debugging can be a challenge."
                    }
                ],
                "target_output": "True"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Finish Python project for presentation.",
                "recent_ocr": "Chocolate Chip Cookies Recipe\n\nIngredients:\n• 2 1/4 cups all-purpose flour\n• 1 teaspoon baking soda\n• 1 teaspoon salt\n• 1 cup unsalted butter, softened\n• 3/4 cup granulated sugar\n• 3/4 cup packed brown sugar\n• 1 teaspoon vanilla extract\n• 2 large eggs\n• 2 cups semi-sweet chocolate chips\n\nInstructions:\n1. Preheat oven to 375°F (190°C).\n2. Combine flour, baking soda and salt in small bowl.\n3. Beat butter, granulated sugar, brown sugar and vanilla extract in large mixer bowl until creamy.\n4. Add eggs, one at a time, beating well after each addition.\n5. Gradually beat in flour mixture.\n6. Stir in chocolate chips.\n7. Drop by rounded tablespoon onto ungreased baking sheets.\n8. Bake for 9 to 11 minutes or until golden brown.\n9. Cool on baking sheets for 2 minutes; remove to wire racks to cool completely.\n\nEnjoy your homemade chocolate chip cookies!",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Chocolate Chip Cookies Recipe\n\nIngredients:\n• 2 1/4 cups all-purpose flour\n• 1 teaspoon baking soda\n• 1 teaspoon salt\n• 1 cup unsalted butter, softened\n• 3/4 cup granulated sugar\n• 3/4 cup packed brown sugar\n• 1 teaspoon vanilla extract\n• 2 large eggs\n• 2 cups semi-sweet chocolate chips\n\nInstructions:\n1. Preheat oven to 375°F (190°C).\n2. Combine flour, baking soda and salt in small bowl.\n3. Beat butter, granulated sugar, brown sugar and vanilla extract in large mixer bowl until creamy.\n4. Add eggs, one at a time, beating well after each addition.\n5. Gradually beat in flour mixture.\n6. Stir in chocolate chips.\n7. Drop by rounded tablespoon onto ungreased baking sheets.\n8. Bake for 9 to 11 minutes or until golden brown.\n9. Cool on baking sheets for 2 minutes; remove to wire racks to cool completely.\n\nEnjoy your homemade chocolate chip cookies!"
                    },
                    {
                        "role": "assistant",
                        "content": "Hi, Sam. How's it going? I noticed currently exploring your MacBook Pro settings, but I'm not clear on how this activity aligns with your current goals. Can you help me understand what you're trying to accomplish?"
                    },
                    {
                        "role": "user",
                        "content": "I'm trying to debug a problem."
                    },
                    {
                        "role": "assistant",
                        "content": "Debugging can be a challenge."
                    }
                ],
                "target_output": "False"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Finish Python project for presentation.",
                "recent_ocr": "Pydantic Documentation\n\nPydantic is a Python library for data validation and settings management using Python type annotations.\n\nQuick start\n\nHere's a quick example of how to use Pydantic:\n\nfrom datetime import datetime\nfrom typing import List, Optional\nfrom pydantic import BaseModel\n\nclass User(BaseModel):\n    id: int\n    name = 'John Doe'\n    signup_ts: Optional[datetime] = None\n    friends: List[int] = []\n\nexternal_data = {\n    'id': '123',\n    'signup_ts': '2019-06-01 12:22',\n    'friends': [1, 2, '3'],\n}\nuser = User(**external_data)\nprint(user.id)\n#> 123\nprint(repr(user.signup_ts))\n#> datetime.datetime(2019, 6, 1, 12, 22)\nprint(user.friends)\n#> [1, 2, 3]\nprint(user.dict())\n\nKey Features:\n• No batteries included — Pydantic tries to use standard Python and only includes what's necessary.\n• Fast — In benchmarks Pydantic is faster than all other tested libraries.\n• Validate complex structures — Use of recursive Pydantic models, Python typing and custom validation.\n• Extensible — Pydantic allows custom data types to be defined or you can extend validation with methods on a model decorated with the validator decorator.\n• Data conversion — Pydantic will convert data to the correct type where possible.\n• Strict mode — Pydantic can be configured to be more strict and raise errors where other libraries would silently allow invalid data.",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Q Search\nSam Stowers\nApple ID\nRcT\nFamily\nWi-Fi\n*\nBluetooth\nNetwork\nNotifications\n4））\nSound\nFocus\nScreen Time\nGeneral\nAppearance\nt Accessibility\n20\nControl Center\nSiri & Spotlight\n山\nPrivacy & Security\nDesktop & Dock\nDinlowo\nSound\nSound Effects\nAlert sound\nPlay sound effects through\nAlert volume\nPlay sound on startup\n』\nPlay user interface sound effects\nPlay feedback when volume is changed\nBoop\nSelected Sound Output Device\nOutput &Input\nOutput\nInput\nName\nExternal Microphone\nMacBook Pro Microphone\nPrivo1\nDemiurgeMobile Microphone\nInput volume\nInput level\nType\nMicrophone port\nBuilt-in\nBluetooth\nContinuity Camera\n沁\n"
                    },
                    {
                        "role": "assistant",
                        "content": "Hi, Sam. How's it going? I noticed currently exploring your MacBook Pro settings, but I'm not clear on how this activity aligns with your current goals. Can you help me understand what you're trying to accomplish?"
                    },
                    {
                        "role": "user",
                        "content": "I'm trying to debug a problem."
                    },
                    {
                        "role": "assistant",
                        "content": "Debugging can be a challenge."
                    }
                ],
                "target_output": "True"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Write a blog post about lasagna.",
                "recent_ocr": "JavaScript ES6 Features\n\nlet and const\nlet allows you to declare variables that are limited to the scope of a block statement, or expression on which it is used.\nconst is used to declare constants, whose values cannot be reassigned.\n\nArrow Functions\nArrow functions allow us to write shorter function syntax:\n\nlet myFunction = (a, b) => a * b;\n\nTemplate Literals\nTemplate literals are string literals allowing embedded expressions.\n\n`string text ${expression} string text`\n\nDestructuring Assignment\nThe destructuring assignment syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.\n\nlet a, b, rest;\n[a, b] = [10, 20];\n\nconsole.log(a); // 10\nconsole.log(b); // 20\n\n[a, b, ...rest] = [10, 20, 30, 40, 50];\n\nconsole.log(rest); // [30, 40, 50]\n\nPromises\nA Promise is an object representing the eventual completion or failure of an asynchronous operation.\n\nlet myPromise = new Promise((resolve, reject) => {\n  // do something asynchronous which eventually calls either:\n  //\n  //   resolve(someValue); // fulfilled\n  // or\n  //   reject('failure reason'); // rejected\n});\n\nClasses\nJavaScript classes are primarily syntactical sugar over JavaScript's existing prototype-based inheritance.\n\nclass Rectangle {\n  constructor(height, width) {\n    this.height = height;\n    this.width = width;\n  }\n}\n\nModules\nModules let you split your code base into multiple files for better organization.\n\n// file math.js\nexport function add(x, y) {\n  return x + y;\n}\n\n// main.js\nimport { add } from './math.js';\n\nconsole.log(add(1, 2)); // 3",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Q Search\nSam Stowers\nApple ID\nRcT\nFamily\nWi-Fi\n*\nBluetooth\nNetwork\nNotifications\n4））\nSound\nFocus\nScreen Time\nGeneral\nAppearance\nt Accessibility\n20\nControl Center\nSiri & Spotlight\n山\nPrivacy & Security\nDesktop & Dock\nDinlowo\nSound\nSound Effects\nAlert sound\nPlay sound effects through\nAlert volume\nPlay sound on startup\n』\nPlay user interface sound effects\nPlay feedback when volume is changed\nBoop\nSelected Sound Output Device\nOutput &Input\nOutput\nInput\nName\nExternal Microphone\nMacBook Pro Microphone\nPrivo1\nDemiurgeMobile Microphone\nInput volume\nInput level\nType\nMicrophone port\nBuilt-in\nBluetooth\nContinuity Camera\n沁\n"
                    },
                    {
                        "role": "assistant",
                        "content": "Hi, Sam. How's it going? I noticed currently exploring your MacBook Pro settings, but I'm not clear on how this activity aligns with your current goals. Can you help me understand what you're trying to accomplish?"
                    },
                    {
                        "role": "user",
                        "content": "I'm trying to debug a problem."
                    },
                    {
                        "role": "assistant",
                        "content": "Debugging can be a challenge."
                    }
                ],
                "target_output": "False"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Answer important work emails.",
                "recent_ocr": "Facebook\nNews Feed\nFriends\nMarketplace\nGroups\nWatch\nMemories\nSaved\nPages\nEvents\nMost Recent\nFavorites\nAd Center\nAds Manager\nClimate Science Center\nCrisis Response\nFundraiser\nGaming Video\nLive Videos\nMessenger\nMeta Quest\nMost Recent\nPlay Games\nRecent Ad Activity\nWeather",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Facebook\nNews Feed\nFriends\nMarketplace\nGroups\nWatch\nMemories\nSaved\nPages\nEvents\nMost Recent\nFavorites\nAd Center\nAds Manager\nClimate Science Center\nCrisis Response\nFundraiser\nGaming Video\nLive Videos\nMessenger\nMeta Quest\nMost Recent\nPlay Games\nRecent Ad Activity\nWeather"
                    },
                ],
                "target_output": "False"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Complete Python coding assignment.",
                "recent_ocr": "Gmail\nInbox (1,254)\nStarred\nSnoozed\nSent\nDrafts (15)\nMore\nImportant\nChats\nScheduled\nAll Mail\nSpam (24)\nTrash\nCategories\nSocial\nUpdates\nForums\nPromotions\nPrimary\nCompose\nMeet\nNew meeting\nJoin a meeting",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Gmail\nInbox (1,254)\nStarred\nSnoozed\nSent\nDrafts (15)\nMore\nImportant\nChats\nScheduled\nAll Mail\nSpam (24)\nTrash\nCategories\nSocial\nUpdates\nForums\nPromotions\nPrimary\nCompose\nMeet\nNew meeting\nJoin a meeting"
                    },
                ],
                "target_output": "False"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Prepare presentation for tomorrow's meeting.",
                "recent_ocr": "Netflix\nTV Shows\nMovies\nNew & Popular\nMy List\nBrowse by Languages\nTrending Now\n1. Stranger Things\n2. Wednesday\n3. Bridgerton\n4. Squid Game\n5. Money Heist\n6. The Witcher\n7. Ozark\n8. The Crown\n9. Lupin\n10. You",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Netflix\nTV Shows\nMovies\nNew & Popular\nMy List\nBrowse by Languages\nTrending Now\n1. Stranger Things\n2. Wednesday\n3. Bridgerton\n4. Squid Game\n5. Money Heist\n6. The Witcher\n7. Ozark\n8. The Crown\n9. Lupin\n10. You"
                    },
                ],
                "target_output": "False"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Research and write article on climate change.",
                "recent_ocr": "Amazon.com\nToday's Deals\nCustomer Service\nRegistry\nGift Cards\nSell\nBestsellers\nAmazon Basics\nNew Releases\nCustomer Service\nPrime\nBooks\nPharmacy\nAmazon Home\nFashion\nKindle Books\nGift Cards\nToys & Games\nAmazon Home\nComputers\nCoupons\nHome Improvement\nBeauty & Personal Care\nPet Supplies\nTV & Video\nHandmade\nBaby",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Amazon.com\nToday's Deals\nCustomer Service\nRegistry\nGift Cards\nSell\nBestsellers\nAmazon Basics\nNew Releases\nCustomer Service\nPrime\nBooks\nPharmacy\nAmazon Home\nFashion\nKindle Books\nGift Cards\nToys & Games\nAmazon Home\nComputers\nCoupons\nHome Improvement\nBeauty & Personal Care\nPet Supplies\nTV & Video\nHandmade\nBaby"
                    },
                ],
                "target_output": "False"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Practice guitar for upcoming recital.",
                "recent_ocr": "Twitter\nHome\nExplore\nNotifications\nMessages\nBookmarks\nLists\nProfile\nMore\nTweet\nWhat's happening\nCOVID-19 · LIVE\nCOVID-19: News and updates for your area\nTrending with #COVID19\nWorld news · LIVE\nLatest updates on global events\nUS news · Trending\n#Election2024\n145K Tweets\nSports · Trending\n#WorldCup2026\n95.5K Tweets\nEntertainment · Trending\nNew Taylor Swift album announced\n500K Tweets",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: Twitter\nHome\nExplore\nNotifications\nMessages\nBookmarks\nLists\nProfile\nMore\nTweet\nWhat's happening\nCOVID-19 · LIVE\nCOVID-19: News and updates for your area\nTrending with #COVID19\nWorld news · LIVE\nLatest updates on global events\nUS news · Trending\n#Election2024\n145K Tweets\nSports · Trending\n#WorldCup2026\n95.5K Tweets\nEntertainment · Trending\nNew Taylor Swift album announced\n500K Tweets"
                    },
                ],
                "target_output": "False"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Fix production bug in the authentication service.",
                "recent_ocr": "Visual Studio Code\nExplorer\nSEARCH\nOUTLINE\nTIMELINE\nauth-service\nsrc\nmodels\ncontrollers\nroutes\nutils\nauth.js\npackage.json\nREADME.md\n\nJIRA-1234: Fix authentication token expiration\nStatus: In Progress\nAssignee: John Doe\nDescription: Users are being logged out unexpectedly due to incorrect token expiration handling.\n\nauth.js\n\nfunction validateToken(token) {\n  // TODO: Fix token expiration check\n  const decoded = jwt.verify(token, process.env.JWT_SECRET);\n  if (decoded.exp <= Date.now() / 1000) {\n    throw new Error('Token has expired');\n  }\n  return decoded;\n}",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: [The OCR text as shown above]"
                    },
                ],
                "target_output": "True"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Research and write an article on renewable energy sources.",
                "recent_ocr": "Google Scholar\nAll\nSince 2023\nSort by relevance\nSort by date\ninclude patents\ninclude citations\n\nRenewable Energy: A Comprehensive Overview of Sources, Technologies, and Future Prospects\nJ. Smith, A. Johnson - Renewable and Sustainable Energy Reviews, 2023\nCited by 145\nRelated articles\nAll 5 versions\n\nComparative Analysis of Solar, Wind, and Hydroelectric Power: Efficiency and Environmental Impact\nM. Garcia, L. Chen - Journal of Clean Energy Production, 2023\nCited by 89\nRelated articles\nAll 3 versions\n\nEmerging Trends in Energy Storage Technologies for Renewable Integration\nK. Patel, R. Williams - Energy Storage Materials, 2023\nCited by 112\nRelated articles\nAll 4 versions",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: [The OCR text as shown above]"
                    },
                ],
                "target_output": "True"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Improve Python programming skills, particularly in data analysis.",
                "recent_ocr": "Jupyter Notebook\nFile Edit View Insert Cell Kernel Help\n\nIn [1]:\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\n# Load the dataset\ndf = pd.read_csv('sales_data.csv')\n\n# Display first few rows\nprint(df.head())\n\n# Basic statistical summary\nprint(df.describe())\n\n# Create a correlation heatmap\nplt.figure(figsize=(10, 8))\nsns.heatmap(df.corr(), annot=True, cmap='coolwarm')\nplt.title('Correlation Heatmap of Sales Data')\nplt.show()\n\nIn [2]:",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: [The OCR text as shown above]"
                    },
                ],
                "target_output": "True"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Prepare for upcoming job interview at a tech company.",
                "recent_ocr": "LeetCode\nProblems\nContest\nDiscuss\nInterview\n\nProblem: Two Sum\nDifficulty: Easy\n\nGiven an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\n\nYou can return the answer in any order.\n\nExample 1:\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].\n\nclass Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        # Your code here",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: [The OCR text as shown above]"
                    },
                ],
                "target_output": "True"
            },
            {
                "self": "weave:///wandb/shoulder-angel/object/GeminiOnTaskAnalyzer:YENyTiSmq3f3QTbMk0uskrY9MPtwJzAKnvc9uQz2iRU",
                "user_goals": "Current goals: Learn about machine learning algorithms for a university project.",
                "recent_ocr": "Coursera\nMachine Learning Specialization\nby Andrew Ng\n\nWeek 3: Logistic Regression\n\nVideo: Logistic Regression Model\nVideo: Decision Boundary\nReading: Logistic Regression Cost Function\nQuiz: Logistic Regression\nProgramming Assignment: Logistic Regression with NumPy\n\nDiscussion Forums\nCourse Resources\nGrades\n\nNext up: Video - Logistic Regression Model (15 min)\n\nIn this video, you will learn:\n- The motivation for logistic regression\n- The sigmoid function\n- How to interpret the output of logistic regression\n- The decision boundary concept",
                "recent_messages": [
                    {
                        "role": "system",
                        "content": "Your name is Angel, short for Shoulder Angel. You are a voice agent on a phone call. Your goal is to help a user stay on track for their goals for the day. End the conversation if A) they were actually focused on the right thing and you called them in error, B) they were distracted and are refocusing, or C) they otherwise request the conversation to end. If you have no memories of their goals, ask what they are."
                    },
                    {
                        "role": "system",
                        "content": "Here is the most recent OCR of the user's screen: [The OCR text as shown above]"
                    },
                ],
                "target_output": "True"
            },
        ]
    )
)
