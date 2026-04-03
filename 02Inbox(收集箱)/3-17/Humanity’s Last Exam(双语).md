# Humanity’s Last Exam  人类的最终考验

###### Abstract  摘要

Benchmarks are important tools for tracking the rapid advancements in large language model (LLM) capabilities. However, benchmarks are not keeping pace in difficulty: LLMs now achieve over 90% accuracy on popular benchmarks like MMLU, limiting informed measurement of state-of-the-art LLM capabilities. In response, we introduce Humanity’s Last Exam (HLE), a multi-modal benchmark at the frontier of human knowledge, designed to be the final closed-ended academic benchmark of its kind with broad subject coverage. HLE consists of 3,000 questions across dozens of subjects, including mathematics, humanities, and the natural sciences. HLE is developed globally by subject-matter experts and consists of multiple-choice and short-answer questions suitable for automated grading. Each question has a known solution that is unambiguous and easily verifiable, but cannot be quickly answered via internet retrieval. State-of-the-art LLMs demonstrate low accuracy and calibration on HLE, highlighting a significant gap between current LLM capabilities and the expert human frontier on closed-ended academic questions. To inform research and policymaking upon a clear understanding of model capabilities, we publicly release HLE at [https://lastexam.ai](https://lastexam.ai/).  
基准测试是追踪大型语言模型（LLM）能力快速进步的重要工具。然而，基准测试的难度未能同步提升：目前 LLMs 在 MMLU 等流行基准测试上的准确率已超过 90%，这限制了对最先进 LLM 能力的有力评估。为此，我们推出了"人类终极考试"（HLE），这是一个处于人类知识前沿的多模态基准测试，旨在成为涵盖广泛学科、同类中最终版的封闭式学术基准。HLE 包含 3,000 道题目，覆盖数学、人文和自然科学等数十个学科。HLE 由全球各学科领域的专家共同开发，包含适合自动评分的多项选择题和简答题。每道题目都有明确且易于验证的已知答案，但无法通过互联网检索快速获得。最先进的 LLMs 在 HLE 上表现出较低的准确率和校准度，凸显了当前 LLM 能力与人类专家在封闭式学术问题前沿水平之间的显著差距。 为了在清晰理解模型能力的基础上为研究和政策制定提供参考，我们在 https://lastexam.ai 上公开发布了 HLE。

### Organizing Team  组织团队

Long Phan∗1, Alice Gatti∗1, Ziwen Han∗2, Nathaniel Li∗1,

Josephina Hu2, Hugh Zhang‡, Sean Shi2, Michael Choi2, Anish Agrawal2, Arnav Chopra2, Adam Khoja1, Ryan Kim†, Richard Ren1, Jason Hausenloy1, Oliver Zhang1, Mantas Mazeika1,

Summer Yue∗∗2, Alexandr Wang∗∗2, Dan Hendrycks∗∗1  
夏月 ∗∗2 、亚历山德·王 ∗∗2 、丹·亨德里克斯 ∗∗1

1 Center for AI Safety, 2 Scale AI  
1 人工智能安全中心， 2 Scale AI

††∗Co-first Authors. ∗∗ Senior Authors. † Work conducted while at Center for AI Safety. ‡ Work conducted while at Scale AI. Complete list of author affiliations in [Appendix˜A](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A1 "Appendix A Authors ‣ Humanity’s Last Exam"). Correspondence to [agibenchmark@safe.ai](https://ar5iv.labs.arxiv.org/html/agibenchmark@safe.ai).

### Dataset Contributors  数据集贡献者

Daron Anderson, Tung Nguyen, Mobeen Mahmood, Fiona Feng, Steven Y. Feng, Haoran Zhao, Michael Yu, Varun Gangal, Chelsea Zou, Zihan Wang, Jessica P. Wang, Pawan Kumar, Oleksandr Pokutnyi, Robert Gerbicz, Serguei Popov, John-Clark Levin, Mstyslav Kazakov, Johannes Schmitt, Geoff Galgon, Alvaro Sanchez, Yongki Lee, Will Yeadon, Scott Sauers, Marc Roth, Chidozie Agu, Søren Riis, Fabian Giska, Saiteja Utpala, Zachary Giboney, Gashaw M. Goshu, Joan of Arc Xavier, Sarah-Jane Crowson, Mohinder Maheshbhai Naiya, Noah Burns, Lennart Finke, Zerui Cheng, Hyunwoo Park, Francesco Fournier-Facio, John Wydallis, Mark Nandor, Ankit Singh, Tim Gehrunger, Jiaqi Cai, Ben McCarty, Darling Duclosel, Jungbae Nam, Jennifer Zampese, Ryan G. Hoerr, Aras Bacho, Gautier Abou Loume, Abdallah Galal, Hangrui Cao, Alexis C Garretson, Damien Sileo, Qiuyu Ren, Doru Cojoc, Pavel Arkhipov, Usman Qazi, Lianghui Li, Sumeet Motwani, Christian Schroeder de Witt, Edwin Taylor, Johannes Veith, Eric Singer, Taylor D. Hartman, Paolo Rissone, Jaehyeok Jin, Jack Wei Lun Shi, Chris G. Willcocks, Joshua Robinson, Aleksandar Mikov, Ameya Prabhu, Longke Tang, Xavier Alapont, Justine Leon Uro, Kevin Zhou, Emily de Oliveira Santos, Andrey Pupasov Maksimov, Edward Vendrow, Kengo Zenitani, Julien Guillod, Yuqi Li, Joshua Vendrow, Vladyslav Kuchkin, Ng Ze-An, Pierre Marion, Denis Efremov, Jayson Lynch, Kaiqu Liang, Andrew Gritsevskiy, Dakotah Martinez, Ben Pageler, Nick Crispino, Dimitri Zvonkine, Natanael Wildner Fraga, Saeed Soori, Ori Press, Henry Tang, Julian Salazar, Sean R. Green, Lina Brüssel, Moon Twayana, Aymeric Dieuleveut, T. Ryan Rogers, Wenjin Zhang, Bikun Li, Jinzhou Yang, Arun Rao, Gabriel Loiseau, Mikhail Kalinin, Marco Lukas, Ciprian Manolescu, Subrata Mishra, Ariel Ghislain Kemogne Kamdoum, Tobias Kreiman, Tad Hogg, Alvin Jin, Carlo Bosio, Gongbo Sun, Brian P Coppola, Tim Tarver, Haline Heidinger, Rafael Sayous, Stefan Ivanov, Joseph M Cavanagh, Jiawei Shen, Joseph Marvin Imperial, Philippe Schwaller, Shaipranesh Senthilkuma, Andres M Bran, Ali Dehghan, Andres Algaba, Brecht Verbeken, David Noever, Ragavendran P V, Lisa Schut, Ilia Sucholutsky, Evgenii Zheltonozhskii, Derek Lim, Richard Stanley, Shankar Sivarajan, Tong Yang, John Maar, Julian Wykowski, Martí Oller, Jennifer Sandlin, Anmol Sahu, Yuzheng Hu, Sara Fish, Nasser Heydari, Archimedes Apronti, Kaivalya Rawal, Tobias Garcia Vilchis, Yuexuan Zu, Martin Lackner, James Koppel, Jeremy Nguyen, Daniil S. Antonenko, Steffi Chern, Bingchen Zhao, Pierrot Arsene, Alan Goldfarb, Sergey Ivanov, Rafał Poświata, Chenguang Wang, Daofeng Li, Donato Crisostomi, Andrea Achilleos, Benjamin Myklebust, Archan Sen, David Perrella, Nurdin Kaparov, Mark H Inlow, Allen Zang, Elliott Thornley, Daniil Orel, Vladislav Poritski, Shalev Ben-David, Zachary Berger, Parker Whitfill, Michael Foster, Daniel Munro, Linh Ho, Dan Bar Hava, Aleksey Kuchkin, Robert Lauff, David Holmes, Frank Sommerhage, Keith Schneider, Zakayo Kazibwe, Nate Stambaugh, Mukhwinder Singh, Ilias Magoulas, Don Clarke, Dae Hyun Kim, Felipe Meneguitti Dias, Veit Elser, Kanu Priya Agarwal, Victor Efren Guadarrama Vilchis, Immo Klose, Christoph Demian, Ujjwala Anantheswaran, Adam Zweiger, Guglielmo Albani, Jeffery Li, Nicolas Daans, Maksim Radionov, Václav Rozhoň, Ziqiao Ma, Christian Stump, Mohammed Berkani, Jacob Platnick, Volodymyr Nevirkovets, Luke Basler, Marco Piccardo, Ferenc Jeanplong, Niv Cohen, Josef Tkadlec, Paul Rosu, Piotr Padlewski, Stanislaw Barzowski, Kyle Montgomery, Aline Menezes, Arkil Patel, Zixuan Wang, Jamie Tucker-Foltz, Jack Stade, Tom Goertzen, Fereshteh Kazemi, Jeremiah Milbauer, John Arnold Ambay, Abhishek Shukla, Yan Carlos Leyva Labrador, Alan Givré, Hew Wolff, Vivien Rossbach, Muhammad Fayez Aziz, Younesse Kaddar, Yanxu Chen, Robin Zhang, Jiayi Pan, Antonio Terpin, Niklas Muennighoff, Hailey Schoelkopf, Eric Zheng, Avishy Carmi, Adam Jones, Jainam Shah, Ethan D. L. Brown, Kelin Zhu, Max Bartolo, Richard Wheeler, Andrew Ho, Shaul Barkan, Jiaqi Wang, Martin Stehberger, Egor Kretov, Kaustubh Sridhar, Zienab EL-Wasif, Anji Zhang, Daniel Pyda, Joanna Tam, David M. Cunningham, Vladimir Goryachev, Demosthenes Patramanis, Michael Krause, Andrew Redenti, Daniel Bugas, David Aldous, Jesyin Lai, Shannon Coleman, Mohsen Bahaloo, Jiangnan Xu, Sangwon Lee, Sandy Zhao, Ning Tang, Michael K. Cohen, Micah Carroll, Orr Paradise, Jan Hendrik Kirchner, Stefan Steinerberger, Maksym Ovchynnikov, Jason O. Matos, Adithya Shenoy, Benedito Alves de Oliveira Junior, Michael Wang, Yuzhou Nie, Paolo Giordano, Philipp Petersen, Anna Sztyber-Betley, Priti Shukla, Jonathan Crozier, Antonella Pinto, Shreyas Verma, Prashant Joshi, Zheng-Xin Yong, Allison Tee, Jérémy Andréoletti, Orion Weller, Raghav Singhal, Gang Zhang, Alexander Ivanov, Seri Khoury, Hamid Mostaghimi, Kunvar Thaman, Qijia Chen, Tran Quoc Khánh, Jacob Loader, Stefano Cavalleri, Hannah Szlyk, Zachary Brown, Jonathan Roberts, William Alley, Kunyang Sun, Ryan Stendall, Max Lamparth, Anka Reuel, Ting Wang, Hanmeng Xu, Sreenivas Goud Raparthi, Pablo Hernández-Cámara, Freddie Martin, Dmitry Malishev, Thomas Preu, Tomek Korbak, Marcus Abramovitch, Dominic Williamson, Ziye Chen, Biró Bálint, M Saiful Bari, Peyman Kassani, Zihao Wang, Behzad Ansarinejad, Laxman Prasad Goswami, Yewen Sun, Hossam Elgnainy, Daniel Tordera, George Balabanian, Earth Anderson, Lynna Kvistad, Alejandro José Moyano, Rajat Maheshwari, Ahmad Sakor, Murat Eron, Isaac C. McAlister, Javier Gimenez, Innocent Enyekwe, Andrew Favre D.O., Shailesh Shah, Xiaoxiang Zhou, Firuz Kamalov, Ronald Clark, Sherwin Abdoli, Tim Santens, Khalida Meer, Harrison K Wang, Kalyan Ramakrishnan, Evan Chen, Alessandro Tomasiello, G. Bruno De Luca, Shi-Zhuo Looi, Vinh-Kha Le, Noam Kolt, Niels Mündler, Avi Semler, Emma Rodman, Jacob Drori, Carl J Fossum, Milind Jagota, Ronak Pradeep, Honglu Fan, Tej Shah, Jonathan Eicher, Michael Chen, Kushal Thaman, William Merrill, Carter Harris, Jason Gross, Ilya Gusev, Asankhaya Sharma, Shashank Agnihotri, Pavel Zhelnov, Siranut Usawasutsakorn, Mohammadreza Mofayezi, Sergei Bogdanov, Alexander Piperski, Marc Carauleanu, David K. Zhang, Dylan Ler, Roman Leventov, Ignat Soroko, Thorben Jansen, Pascal Lauer, Joshua Duersch, Vage Taamazyan, Wiktor Morak, Wenjie Ma, William Held, Tran Đuc Huy, Ruicheng Xian, Armel Randy Zebaze, Mohanad Mohamed, Julian Noah Leser, Michelle X Yuan, Laila Yacar, Johannes Lengler, Hossein Shahrtash, Edson Oliveira, Joseph W. Jackson, Daniel Espinosa Gonzalez, Andy Zou, Muthu Chidambaram, Timothy Manik, Hector Haffenden, Dashiell Stander, Ali Dasouqi, Alexander Shen, Emilien Duc, Bita Golshani, David Stap, Mikalai Uzhou, Alina Borisovna Zhidkovskaya, Lukas Lewark, Mátyás Vincze, Dustin Wehr, Colin Tang, Zaki Hossain, Shaun Phillips, Jiang Muzhen, Fredrik Ekström, Angela Hammon, Oam Patel, Nicolas Remy, Faraz Farhidi, George Medley, Forough Mohammadzadeh, Madellene Peñaflor, Haile Kassahun, Alena Friedrich, Claire Sparrow, Taom Sakal, Omkar Dhamane, Ali Khajegili Mirabadi, Eric Hallman, Mike Battaglia, Mohammad Maghsoudimehrabani, Hieu Hoang, Alon Amit, Dave Hulbert, Roberto Pereira, Simon Weber, Stephen Mensah, Nathan Andre, Anton Peristyy, Chris Harjadi, Himanshu Gupta, Stephen Malina, Samuel Albanie, Will Cai, Mustafa Mehkary, Frank Reidegeld, Anna-Katharina Dick, Cary Friday, Jasdeep Sidhu, Wanyoung Kim, Mariana Costa, Hubeyb Gurdogan, Brian Weber, Harsh Kumar, Tong Jiang, Arunim Agarwal, Chiara Ceconello, Warren S. Vaz, Chao Zhuang, Haon Park, Andrew R. Tawfeek, Daattavya Aggarwal, Michael Kirchhof, Linjie Dai, Evan Kim, Johan Ferret, Yuzhou Wang, Minghao Yan, Krzysztof Burdzy, Lixin Zhang, Antonio Franca, Diana T. Pham, Kang Yong Loh, Joshua Robinson, Shreen Gul, Gunjan Chhablani, Zhehang Du, Adrian Cosma, Colin White, Robin Riblet, Prajvi Saxena, Jacob Votava, Vladimir Vinnikov, Ethan Delaney, Shiv Halasyamani, Syed M. Shahid, Jean-Christophe Mourrat, Lavr Vetoshkin, Renas Bacho, Vincent Ginis, Aleksandr Maksapetyan, Florencia de la Rosa, Xiuyu Li, Guillaume Malod, Leon Lang, Julien Laurendeau, Fatimah Adesanya, Julien Portier, Lawrence Hollom, Victor Souza, Yuchen Anna Zhou, Yiğit Yalın, Gbenga Daniel Obikoya, Luca Arnaboldi, Rai (Michael Pokorny), Filippo Bigi, Kaniuar Bacho, Pierre Clavier, Gabriel Recchia, Mara Popescu, Nikita Shulga, Ngefor Mildred Tanwie, Thomas C.H. Lux, Ben Rank, Colin Ni, Alesia Yakimchyk, Huanxu (Quinn) Liu, Olle Häggström, Emil Verkama, Himanshu Narayan, Hans Gundlach, Leonor Brito-Santana, Brian Amaro, Vivek Vajipey, Rynaa Grover, Yiyang Fan, Gabriel Poesia Reis e Silva, Linwei Xin, Yosi Kratish, Jakub Łucki, Wen-Ding Li, Justin Xu, Kevin Joseph Scaria, Freddie Vargus, Farzad Habibi, Long (Tony) Lian, Emanuele Rodolà, Jules Robins, Vincent Cheng, Declan Grabb, Ida Bosio, Tony Fruhauff, Ido Akov, Eve J. Y. Lo, Hao Qi, Xi Jiang, Ben Segev, Jingxuan Fan, Sarah Martinson, Erik Y. Wang, Kaylie Hausknecht, Michael P. Brenner, Mao Mao, Yibo Jiang, Xinyu Zhang, David Avagian, Eshawn Jessica Scipio, Muhammad Rehan Siddiqi, Alon Ragoler, Justin Tan, Deepakkumar Patil, Rebeka Plecnik, Aaron Kirtland, Roselynn Grace Montecillo, Stephane Durand, Omer Faruk Bodur, Zahra Adoul, Mohamed Zekry, Guillaume Douville, Ali Karakoc, Tania C. B. Santos, Samir Shamseldeen, Loukmane Karim, Anna Liakhovitskaia, Nate Resman, Nicholas Farina, Juan Carlos Gonzalez, Gabe Maayan, Sarah Hoback, Rodrigo De Oliveira Pena, Glen Sherman, Hodjat Mariji, Rasoul Pouriamanesh, Wentao Wu, Gözdenur Demir, Sandra Mendoza, Ismail Alarab, Joshua Cole, Danyelle Ferreira, Bryan Johnson, Hsiaoyun Milliron, Mohammad Safdari, Liangti Dai, Siriphan Arthornthurasuk, Alexey Pronin, Jing Fan, Angel Ramirez-Trinidad, Ashley Cartwright, Daphiny Pottmaier, Omid Taheri, David Outevsky, Stanley Stepanic, Samuel Perry, Luke Askew, Raúl Adrián Huerta Rodríguez, Abdelkader Dendane, Sam Ali, Ricardo Lorena, Krishnamurthy Iyer, Sk Md Salauddin, Murat Islam, Juan Gonzalez, Josh Ducey, Russell Campbell, Maja Somrak, Vasilios Mavroudis, Eric Vergo, Juehang Qin, Benjámin Borbás, Eric Chu, Jack Lindsey, Anil Radhakrishnan, Antoine Jallon, I.M.J. McInnis, Alex Hoover, Sören Möller, Song Bian, John Lai, Tejal Patwardhan  
达伦·安德森、阮东、莫宾·马哈茂德、冯菲奥娜、冯史蒂文、赵浩然、迈克尔·余、瓦伦·甘加尔、切尔西·邹、王子涵、杰西卡·王、帕万·库马尔、奥列克桑德尔·波库特尼、罗伯特·格比茨、谢尔盖·波波夫、约翰-克拉克·莱文、姆斯季斯拉夫·卡扎科夫、约翰内斯·施密特、杰夫·加尔贡、阿尔瓦罗·桑切斯、李永基、威尔·耶登、斯科特·索尔斯、马克·罗斯、奇多齐·阿古、索伦·里斯、法比安·吉斯卡、赛特贾·乌特帕拉、扎卡里·吉博尼、加肖·M·戈舒、圣女贞德·泽维尔、莎拉-简·克劳森、莫欣德·马赫什巴伊·奈亚、诺亚·伯恩斯、伦纳特·芬克、程泽瑞、朴贤宇、弗朗切斯科·富尔尼耶-法西奥、约翰·怀达利斯、马克·南多尔、安基特·辛格、蒂姆·格伦格、蔡佳琪、本·麦卡蒂、达林·杜克洛塞尔、南正培、詹妮弗·赞佩塞、瑞安·G·赫尔、阿拉斯·巴乔、高蒂埃·阿布·卢姆、阿卜杜拉·加拉尔、曹航瑞、亚历克西斯·C·加勒森、达米安·西莱奥、任秋雨、多鲁·科约克、帕维尔·阿尔希波夫、乌斯曼·卡齐、李良辉、苏米特·莫特瓦尼、克里斯蒂安·施罗德·德·维特、埃德温·泰勒、约翰内斯·法伊特、埃里克·辛格、泰勒·D·哈特曼、保罗·里索内、金宰赫、施伟伦、克里斯·G 威尔科克斯，约书亚·罗宾逊，亚历山大·米科夫，阿梅亚·普拉布，唐龙科，泽维尔·阿拉蓬特，贾斯汀·莱昂·乌罗，凯文·周，艾米丽·德·奥利维拉·桑托斯，安德烈·普帕索夫·马克西莫夫，爱德华·文德罗，健吾·泽尼塔尼，朱利安·吉约，李雨琪，约书亚·文德罗，弗拉迪斯拉夫·库奇金，吴泽安，皮埃尔·马里昂，丹尼斯·埃弗雷莫夫，杰森·林奇，梁凯曲，安德鲁·格里采夫斯基，达科塔·马丁内斯，本·帕格勒，尼克·克里斯皮诺，迪米特里·兹冯金，纳塔内尔·维尔德纳·弗拉加，赛义德·苏里，奥里·普雷斯，亨利·唐，朱利安·萨拉查，肖恩·R·格林，莉娜·布鲁塞尔，穆恩·特瓦亚纳，艾默里克·迪厄勒沃，T. 瑞安·罗杰斯、温金·张、比昆·李、金舟·杨、阿伦·拉奥、加布里埃尔·卢瓦索、米哈伊尔·卡利宁、马可·卢卡斯、西普里安·马诺列斯库、苏布拉塔·米什拉、阿里尔·吉斯兰·凯莫涅·卡姆杜姆、托比亚斯·克雷曼、塔德·霍格、阿尔文·金、卡洛·博西奥、孙公博、布莱恩·P·科波拉、蒂姆·塔弗、哈利娜·海丁格、拉斐尔·萨尤斯、斯特凡·伊万诺夫、约瑟夫·M·卡瓦纳、沈家伟、约瑟夫·马文·因佩里亚尔、菲利普·施瓦勒、沙伊普拉内什·森蒂尔库马、安德烈斯·M·布兰、阿里·德赫甘、安德烈斯·阿尔加巴、布雷赫特·韦尔贝肯、大卫·诺弗、拉加文德兰·P·V、丽莎·舒特、伊利亚·苏霍卢茨基、叶夫根尼·热尔托诺日斯基、德里克·林、理查德·斯坦利、尚卡尔·西瓦拉詹、童阳、约翰·马尔、朱利安·维科夫斯基、马蒂·奥勒、詹妮弗·桑德林、安莫尔·萨胡、胡宇正、萨拉·菲什、纳赛尔·海达里、阿基米德·阿普龙蒂、凯瓦利亚·拉瓦尔、托比亚斯·加西亚·维尔奇斯、祖月轩、马丁·拉克纳、詹姆斯·科佩尔、杰里米·阮、丹尼尔·S· 安东年科、斯蒂菲·切尔恩、赵秉辰、皮埃罗·阿尔塞内、艾伦·戈德法布、谢尔盖·伊万诺夫、拉法乌·波希维亚塔、王晨光、李道峰、多纳托·克里斯托斯托米、安德烈亚·阿基莱奥斯、本杰明·米克勒布斯特、阿尔尚·森、大卫·佩雷拉、努尔丁·卡帕罗夫、马克·H·因洛、艾伦·臧、埃利奥特·索恩利、丹尼尔·奥雷尔、弗拉迪斯拉夫·波里茨基、沙莱夫·本-戴维、扎卡里·伯杰、帕克·惠特菲尔、迈克尔·福斯特、丹尼尔·芒罗、林·何、丹·巴尔·哈瓦、阿列克谢·库奇金、罗伯特·劳夫、大卫·霍姆斯、弗兰克·佐默哈格、基思·施耐德、扎卡约·卡齐布韦、内特·斯坦博、穆克温德·辛格、伊利亚斯·马古拉斯、唐·克拉克、金大贤、费利佩·梅内吉蒂·迪亚斯、维特·埃尔瑟、卡努·普里亚·阿加瓦尔、维克托·埃夫伦·瓜达拉马·维尔奇斯、伊莫·克洛泽、克里斯托夫·德米安、乌贾瓦拉·阿南特斯瓦兰、亚当·茨韦格、古列尔莫·阿尔巴尼、杰弗里·李、尼古拉斯·丹斯、马克西姆·拉季奥诺夫、瓦茨拉夫·罗佐霍尼、马子乔、克里斯蒂安·施通普、穆罕默德·贝尔卡尼、雅各布·普拉特尼克、沃洛迪米尔·内维尔科韦茨、卢克·巴斯勒、马尔科·皮卡多、费伦茨·让普隆、尼夫·科恩、约瑟夫·特卡德莱茨、保罗·罗苏、彼得·帕德莱夫斯基、斯坦尼斯瓦夫·巴尔佐夫斯基、凯尔·蒙哥马利、阿琳·梅内泽斯、阿基尔·帕特尔、王子轩、杰米·塔克-福尔茨、杰克·斯特德、汤姆·戈特岑、费雷什特·卡泽米、杰里迈亚·米尔鲍尔、约翰·阿诺德·安巴伊、阿布舍克·舒克拉、 Yan Carlos Leyva Labrador, Alan Givré, Hew Wolff, Vivien Rossbach, Muhammad Fayez Aziz, Younesse Kaddar, Yanxu Chen, Robin Zhang, Jiayi Pan, Antonio Terpin, Niklas Muennighoff, Hailey Schoelkopf, Eric Zheng, Avishy Carmi, Adam Jones, Jainam Shah, Ethan D. L. Brown, Kelin Zhu, Max Bartolo, Richard Wheeler, Andrew Ho, Shaul Barkan, Jiaqi Wang, Martin Stehberger, Egor Kretov, Kaustubh Sridhar, Zienab EL-Wasif, Anji Zhang, Daniel Pyda, Joanna Tam, David M. Cunningham, Vladimir Goryachev, Demosthenes Patramanis, Michael Krause, Andrew Redenti, Daniel Bugas, David Aldous, Jesyin Lai, Shannon Coleman, Mohsen Bahaloo, Jiangnan Xu, Sangwon Lee, Sandy Zhao, Ning Tang, Michael K. Cohen, Micah Carroll, Orr Paradise, Jan Hendrik Kirchner, Stefan Steinerberger, Maksym Ovchynnikov, Jason O. 马托斯、阿迪蒂亚·谢诺伊、小贝内迪托·阿尔维斯·德奥利维拉、迈克尔·王、聂宇舟、保罗·乔达诺、菲利普·彼得森、安娜·什蒂贝尔-贝特利、普里蒂·舒克拉、乔纳森·克罗泽、安东内拉·平托、什雷亚斯·维尔马、普拉尚特·乔希、郑新勇、艾莉森·蒂、杰雷米·安德烈奥莱蒂、奥里昂·韦勒、拉加夫·辛哈尔、张刚、亚历山大·伊万诺夫、塞里·库里、哈米德·莫斯塔吉米、昆瓦尔·塔曼、陈启佳、陈国庆、雅各布·洛德、斯特凡诺·卡瓦莱里、汉娜·斯利克、扎卡里·布朗、乔纳森·罗伯茨、威廉·阿利、孙坤阳、瑞安·斯滕德尔、马克斯·兰帕斯、安卡·鲁埃尔、王婷、徐翰萌、斯里尼瓦斯·古德·拉帕尔蒂、巴勃罗·埃尔南德斯-卡马拉、弗雷迪·马丁、德米特里·马利舍夫、托马斯·普罗伊、托梅克·科尔巴克、马库斯·阿布拉莫维奇、多米尼克·威廉姆森、陈子烨、比罗·巴林特、M·赛富尔·巴里、佩曼·卡萨尼、王子豪、贝赫扎德·安萨里内贾德、拉克什曼·普拉萨德·戈斯瓦米、孙业文、霍萨姆·埃尔格奈尼、丹尼尔·托德拉、乔治·巴拉巴尼安、厄斯·安德森、林娜·克维斯塔德、亚历杭德罗·何塞·莫亚诺、拉贾特·马赫什瓦里、艾哈迈德·萨科尔、穆拉特·埃龙、艾萨克·C·麦卡利斯特、哈维尔·希门尼斯、因诺森特·恩耶奎、安德鲁·法夫尔 D.O., 沙伊莱什·沙阿, 肖翔·周, 菲鲁兹·卡马洛夫, 罗纳德·克拉克, 谢尔温·阿卜杜利, 蒂姆·桑滕斯, 哈利达·米尔, 哈里森·K·王, 卡利安·拉马克里希南, 埃文·陈, 亚历山德罗·托马西耶洛, G. 布鲁诺·德·卢卡, 施卓·卢伊, 文卡·勒, 诺姆·科尔特, 尼尔斯·明德勒, 阿维·塞姆勒, 艾玛·罗德曼, 雅各布·德罗里, 卡尔·J·福瑟姆, 米林德·贾戈塔, 罗纳克·普拉迪普, 洪璐·范, 特杰·沙阿, 乔纳森·艾歇尔, 迈克尔·陈, 库沙尔·塔曼, 威廉·梅里尔, 卡特·哈里斯, 贾森·格罗斯, 伊利亚·古谢夫, 阿桑卡亚·夏尔马, 沙尚克·阿格尼霍特里, 帕维尔·热尔诺夫, 西拉努特·乌萨瓦苏察孔, 穆罕默德礼萨·莫法耶齐, 谢尔盖·博格丹诺夫, 亚历山大·皮佩尔斯基, 马克·卡拉乌莱亚努, 大卫·K·张, 迪伦·勒, 罗曼·莱文托夫, 伊格纳特·索罗科, 托本·扬森, 帕斯卡尔·劳尔, 约书亚·杜尔施, 瓦格·塔马兹扬, 维克托·莫拉克, 文杰·马, 威廉·赫尔德, 陈德辉, 贤瑞成, 阿梅尔·兰迪·泽巴泽, 莫哈纳德·穆罕默德, 朱利安·诺亚·莱瑟, 米歇尔·X·袁, 莱拉·亚卡尔, 约翰内斯·伦格勒, 侯赛因·沙尔塔什, 埃德森·奥利维拉, 约瑟夫·W· 杰克逊、丹尼尔·埃斯皮诺萨·冈萨雷斯、安迪·邹、穆图·奇丹巴拉姆、蒂莫西·马尼克、赫克托·哈芬登、达希尔·斯坦德、阿里·达苏奇、亚历山大·申、埃米利安·杜克、比塔·戈尔沙尼、大卫·斯塔普、米卡莱·乌祖、阿琳娜·鲍里索夫娜·日德科夫斯卡娅、卢卡斯·莱瓦克、马蒂亚斯·文策、达斯汀·韦尔、科林·唐、扎基·侯赛因、肖恩·菲利普斯、姜慕真、弗雷德里克·埃克斯特伦、安吉拉·哈蒙、奥姆·帕特尔、尼古拉斯·雷米、法拉兹·法尔希迪、乔治·梅德利、福鲁·穆罕默德扎德、马德琳·佩尼亚弗洛尔、海勒·卡萨洪、阿莱娜·弗里德里希、克莱尔·斯帕罗、陶姆·萨卡尔、奥姆卡尔·达曼、阿里·哈杰吉利·米拉巴迪、埃里克·霍尔曼、迈克·巴塔利亚、穆罕默德·马格苏迪梅赫拉巴尼、休·黄、阿隆·阿米特、戴夫·赫尔伯特、罗伯托·佩雷拉、西蒙·韦伯、斯蒂芬·门萨、内森·安德烈、安东·佩里斯蒂、克里斯·哈贾迪、希曼舒·古普塔、斯蒂芬·马利纳、塞缪尔·阿尔巴尼、威尔·蔡、穆斯塔法·梅哈卡里、弗兰克·赖德格尔德、安娜-卡特琳娜·迪克、卡里·弗莱迪、贾斯迪普·西杜、万永·金、玛丽安娜·科斯塔、胡贝布·古尔多安、布莱恩·韦伯、哈什·库马尔、童江、阿鲁尼姆·阿加瓦尔、基亚拉·切科内洛、沃伦·S·瓦斯、庄超、朴浩恩、安德鲁·R。 塔菲克、达塔维亚·阿加瓦尔、迈克尔·基尔霍夫、戴林杰、埃文·金、约翰·费雷特、王宇舟、严明浩、克日什托夫·布尔齐、张立新、安东尼奥·弗兰卡、戴安娜·T·范、罗康勇、约书亚·罗宾逊、什林·古尔、古扬·查布拉尼、杜哲航、阿德里安·科斯马、科林·怀特、罗宾·里布莱特、普拉吉维·萨克塞纳、雅各布·沃塔瓦、弗拉基米尔·温尼科夫、伊桑·德莱尼、希夫·哈拉西亚马尼、赛义德·M·沙希德、让-克里斯托夫·穆拉特、拉夫尔·维托什金、雷纳斯·巴乔、文森特·吉尼斯、亚历山大·马克萨佩蒂安、弗洛伦西亚·德拉罗萨、李修宇、纪尧姆·马洛德、莱昂·朗、朱利安·洛朗多、法蒂玛·阿德萨尼亚、朱利安·波蒂尔、劳伦斯·霍洛姆、维克多·索萨、周安娜、伊吉特·亚林、格本加·丹尼尔·奥比科亚、卢卡·阿纳博尔迪、雷（迈克尔·波科尔尼）、菲利波·比吉、卡纽尔·巴乔、皮埃尔·克拉维耶、加布里埃尔·雷基亚、马拉·波佩斯库、尼基塔·舒尔加、恩格福·米尔德里德·坦维、托马斯·C·H。 卢克斯，本·兰克，科林·倪，阿莱西亚·亚基姆奇克，刘焕旭（奎因），奥勒·哈格斯特伦，埃米尔·维尔卡马，希曼舒·纳拉扬，汉斯·冈德拉赫，莱奥诺尔·布里托-桑塔纳，布莱恩·阿马罗，维韦克·瓦吉佩，里娜·格罗弗，范一阳，加布里埃尔·波埃西亚·雷斯·席尔瓦，辛林伟，约西·克拉蒂什，雅各布·武茨基，李文鼎，贾斯汀·徐，凯文·约瑟夫·斯卡里亚，弗雷迪·瓦格斯，法尔扎德·哈比比，梁龙（托尼），埃马努埃莱·罗多拉，朱尔斯·罗宾斯，文森特·郑，德克兰·格拉布，艾达·博西奥，托尼·弗吕霍夫，伊多·阿科夫，伊芙·J·Y·罗，齐浩，蒋曦，本·塞格夫，范景轩，莎拉·马丁森，王奕元，凯莉·豪斯克内希特，迈克尔·P·布伦纳，毛矛，蒋一博，张欣宇，大卫·阿瓦吉安，埃肖恩·杰西卡·西皮奥，穆罕默德·雷汉·西迪基，阿隆·拉戈勒，贾斯汀·谭，迪帕库马尔·帕蒂尔，雷贝卡·普莱奇尼克，亚伦·柯特兰，罗丝琳·格雷斯·蒙特西略，斯特凡·杜兰德，奥马尔·法鲁克·博杜尔，扎赫拉·阿杜尔，穆罕默德·泽克里，纪尧姆·杜维尔，阿里·卡拉科奇，塔尼亚·C·B 桑托斯、萨米尔·沙姆塞尔丁、卢克曼·卡里姆、安娜·利亚霍维茨卡娅、内特·雷斯曼、尼古拉斯·法里纳、胡安·卡洛斯·冈萨雷斯、加布·马扬、莎拉·霍巴克、罗德里戈·德奥利维拉·佩纳、格伦·谢尔曼、霍贾特·马里吉、拉苏尔·普里亚马内什、吴文涛、格兹德努尔·德米尔、桑德拉·门多萨、伊斯梅尔·阿拉拉布、约书亚·科尔、丹耶尔·费雷拉、布莱恩·约翰逊、萧云·米利伦、穆罕默德·萨夫达里、戴良体、西里潘·阿索恩图拉苏克、阿列克谢·普罗宁、范静、安赫尔·拉米雷斯-特里尼达德、阿什利·卡特赖特、达菲尼·波特迈尔、奥米德·塔赫里、大卫·乌特夫斯基、斯坦利·斯特帕尼克、塞缪尔·佩里、卢克·阿斯丘、劳尔·阿德里安·韦尔塔·罗德里格斯、阿卜杜勒卡德尔·丹丹、萨姆·阿里、里卡多·洛雷纳、克里希纳穆尔蒂·艾耶、斯凯·穆罕默德·萨劳丁、穆拉特·伊斯兰、胡安·冈萨雷斯、乔什·杜西、拉塞尔·坎贝尔、玛雅·索姆拉克、瓦西里奥斯·马夫鲁迪斯、埃里克·维尔戈、秦珏航、本雅明·博尔巴斯、埃里克·朱、杰克·林赛、阿尼尔·拉达克里希南、安托万·贾隆、I.M.J. 麦金尼斯、亚历克斯·胡佛、索伦·穆勒、宋边、约翰·赖、特贾尔·帕特瓦丹

††Co-author list in progress. Humanity’s Last Exam is still accepting new questions. New questions can be submitted at [lastexam.ai/submit](https://lastexam.ai/submit) for co-authorship in this section, but are not eligible for the prize pool.

## 1Introduction  1 引言

The capabilities of large language models (LLMs) have progressed dramatically, exceeding human performance across a diverse array of tasks. To systematically measure these capabilities, LLMs are evaluated upon benchmarks: collections of questions which assess model performance on tasks such as math, programming, or biology. However, state-of-the-art LLMs [[34](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib34), [49](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib49), [37](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib37), [16](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib16), [3](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib3), [56](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib56), [14](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib14)] now achieve over 90% accuracy on popular benchmarks such as MMLU [[21](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib21)], which were once challenging frontiers for LLMs. The saturation of existing benchmarks, as shown in [Figure˜1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S1.F1 "In 1 Introduction ‣ Humanity’s Last Exam"), limits our ability to precisely measure AI capabilities and calls for more challenging evaluations that can meaningfully assess the rapid improvements in LLM capabilities at the frontiers of human knowledge.  
大型语言模型（LLMs）的能力已取得显著进步，在多种任务上超越了人类表现。为了系统性地衡量这些能力，LLMs 需通过基准测试进行评估：这些测试集包含一系列问题，用于评估模型在数学、编程或生物学等任务上的表现。然而，当前最先进的 LLMs [34, 49, 37, 16, 3, 56, 14] 在诸如 MMLU [21] 等曾对 LLMs 构成挑战的流行基准测试中，准确率已超过 90%。如图˜1 所示，现有基准测试的饱和限制了我们对 AI 能力进行精确评估的能力，并呼吁开展更具挑战性的评估，以有意义地衡量 LLMs 在人类知识前沿领域快速提升的能力。

To address this gap, we introduce Humanity’s Last Exam (HLE), a benchmark of 3,000 extremely challenging questions from dozens of subject areas, designed to be the final closed-ended benchmark of broad academic capabilities. HLE is developed by academics and domain experts, providing a precise measure of capabilities as LLMs continue to improve ([Section˜3.1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S3.SS1 "3.1 Collection ‣ 3 Dataset ‣ Humanity’s Last Exam")). HLE is multi-modal, featuring questions that are either text-only or accompanied by an image reference, and includes both multiple-choice and exact-match questions for automated answer verification. Questions are original, precise, unambiguous, and resistant to simple internet lookup or database retrieval. Amongst the diversity of questions in the benchmark, HLE emphasizes world-class mathematics problems aimed at testing deep reasoning skills broadly applicable across multiple academic areas.  
为填补这一空白，我们推出了"人类终极考试"（HLE）——一个包含 3,000 数十个学科领域极富挑战性问题的基准测试，旨在成为衡量广泛学术能力的终极封闭式评估标准。HLE 由学术界和领域专家共同开发，随着 LLMs 的持续进步，它能提供精确的能力度量（参见第 3.1 节）。该基准具有多模态特性，既包含纯文本问题，也包含附带图像参考的问题，并采用选择题与精确匹配题相结合的形式以实现自动化答案验证。所有问题均为原创设计，具备精确性、无歧义性，且能有效规避简单的网络搜索或数据库检索。在基准测试的多样化问题中，HLE 特别强调世界级数学难题，旨在检验那些广泛适用于多学科领域的深度推理能力。

We employ a multi-stage review process to thoroughly ensure question difficulty and quality ([Section˜3.2](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S3.SS2 "3.2 Review ‣ 3 Dataset ‣ Humanity’s Last Exam")). Before submission, each question is tested against state-of-the-art LLMs to verify its difficulty - questions are rejected if LLMs can answer them correctly. Questions submitted then proceed through a two-stage reviewing process: (1) an initial feedback round with multiple graduate-level reviewers and (2) organizer and expert reviewer approval, ensuring quality and adherence to our submission criteria. Following release, we plan to further conduct a public review period, welcoming community feedback to correct any points of concern in the dataset.  
我们采用多阶段审核流程，以确保问题的难度和质量得到全面把控（第 3.2 节）。在提交前，每个问题都会经过最先进的 LLMs 测试以验证其难度——如果 LLMs 能够正确回答，该问题将被拒绝。随后，提交的问题会进入两阶段审核流程：（1）由多位研究生级别的评审员进行初步反馈轮次；（2）组织者和专家评审员的最终批准，以确保质量并符合我们的提交标准。发布后，我们计划进一步开展公开评审期，欢迎社区反馈以修正数据集中任何值得关注的问题。

Frontier LLMs consistently demonstrate low accuracy (less than 10%) across all models, highlighting a significant gap between current capabilities and expert-level academic performance ([Section˜4](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4 "4 Evaluation ‣ Humanity’s Last Exam")). Models also provide incorrect answers with high confidence rather than acknowledging uncertainty on these challenging questions, with RMS calibration errors above 80% across all models.  
前沿 LLMs 在所有模型上均表现出较低的正确率（低于 10%），突显出现有能力与专家级学术表现之间存在显著差距（第 4 节）。面对这些具有挑战性的问题，模型不仅未能承认不确定性，反而以高置信度给出错误答案，所有模型的 RMS 校准误差均超过 80%。

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2501.14249/assets/x1.png)

Figure 1:Compared against the saturation of some existing benchmarks, Humanity’s Last Exam accuracy remains low across several frontier models, demonstrating its effectiveness for measuring advanced, closed-ended, academic capabilities. The sources for our evaluation metrics are detailed in [Section˜C.5](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS5 "C.5 Benchmark Difficulty Comparison ‣ Appendix C Evaluation ‣ Humanity’s Last Exam"). We further evaluate more frontier models on HLE in [Table˜1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4.T1 "In Calibration Error. ‣ 4.2 Quantitative Results ‣ 4 Evaluation ‣ Humanity’s Last Exam").  
图 1：与部分现有基准测试的饱和状态相比，《人类终极考试》在多个前沿模型上的正确率仍然偏低，这证明了其在衡量高级、封闭式学术能力方面的有效性。我们评估指标的详细来源见第 C.5 节。我们还在表 1 中进一步评估了更多前沿模型在 HLE 上的表现。

As AI systems approach human expert performance in many domains, precise measurement of their capabilities and limitations is essential for informing research, governance, and the broader public. High performance on HLE would suggest expert-level capabilities on closed-ended academic questions. To establish a common reference point for assessing these capabilities, we publicly release a large number of 3,000 questions from HLE to enable this precise measurement, while maintaining a private test set to assess potential model overfitting.  
随着人工智能系统在诸多领域接近人类专家水平，精确评估其能力与局限对于指导研究、治理及公众认知至关重要。在人类终极考试中取得优异成绩，将意味着模型在封闭式学术问题上具备专家级能力。为建立评估这些能力的共同基准，我们公开发布了大量来自人类终极考试的 3,000 问题，以实现精准评估，同时保留私有测试集以检测潜在的模型过拟合问题。

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2501.14249/assets/x2.png)

Figure 2:Samples of the diverse and challenging questions submitted to Humanity’s Last Exam.  
图 2：提交给“人类终极考试”的多样化且具有挑战性的问题样本。

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2501.14249/assets/x3.png)

Figure 3:HLE consists of 3,000 exam questions in over a hundred subjects, grouped into high level categories here. We provide a more detailed list of subjects in [Section˜B.3](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A2.SS3 "B.3 Subject List ‣ Appendix B Dataset ‣ Humanity’s Last Exam").  
图 3：人类终极考试包含超过一百个科目的 3,000 道考题，此处按高级类别分组。我们在第˜B.3 节提供了更详细的科目列表。

## 2Related Work  2 相关工作

##### LLM Benchmarks.  LLM 基准测试。

Benchmarks are important tools for tracking the rapid advancement of LLM capabilities, including scientific [[21](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib21), [30](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib30), [44](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib44), [53](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib53), [29](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib29), [10](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib10), [47](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib47), [12](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib12), [61](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib61)] and mathematical reasoning [[22](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib22), [31](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib31), [13](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib13), [18](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib18), [45](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib45), [19](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib19), [17](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib17), [50](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib50)], code generation [[10](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib10), [60](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib60), [26](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib26), [11](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib11), [20](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib20), [9](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib9), [6](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib6)], and general-purpose human assistance [[7](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib7), [47](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib47), [54](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib54), [40](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib40), [42](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib42), [43](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib43), [8](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib8), [1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib1), [25](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib25)]. Due to their objectivity and ease of automated scoring at scale, evaluations commonly include multiple-choice and short-answer questions [[42](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib42), [51](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib51), [52](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib52), [58](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib58), [15](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib15)], with benchmarks such as MMLU [[21](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib21)] also spanning a broad range of academic disciplines and levels of complexity.  
基准测试是追踪 LLM 能力快速进步的重要工具，涵盖科学推理[21, 30, 44, 53, 29, 10, 47, 12, 61]与数学推理[22, 31, 13, 18, 45, 19, 17, 50]、代码生成[10, 60, 26, 11, 20, 9, 6]以及通用人类辅助任务[7, 47, 54, 40, 42, 43, 8, 1, 25]等领域。因其客观性及易于大规模自动化评分的特性，评估通常采用选择题与简答题形式[42, 51, 52, 58, 15]，例如 MMLU[21]等基准测试还覆盖了广泛的学科领域与复杂度层级。

##### Saturation and Frontier Benchmark Design.  
基准测试饱和与前沿设计。

However, state-of-the-art models now achieve nearly perfect scores on many existing evaluations [[34](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib34), [49](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib49), [37](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib37), [16](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib16), [3](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib3), [56](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib56), [14](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib14)], obscuring the full extent of current and future frontier AI capabilities [[38](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib38), [39](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib39), [27](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib27), [32](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib32)]. This has motivated the development of more challenging benchmarks which test for multi-modal capabilities [[10](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib10), [53](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib53), [48](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib48), [59](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib59), [2](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib2), [28](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib28), [31](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib31), [26](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib26), [57](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib57), [46](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib46)], strengthen existing benchmarks [[53](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib53), [48](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib48), [24](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib24), [45](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib45), [43](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib43)], filter questions over multiple stages of review [[33](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib33), [30](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib30), [44](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib44), [18](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib18), [27](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib27)], and employ experts to write tests for advanced academic knowledge [[44](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib44), [30](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib30), [18](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib18), [41](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib41), [34](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib34), [5](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib5)]. HLE combines these approaches: the questions are developed by subject-matter experts and undergo multiple rounds of review, while preserving the broad subject-matter coverage of MMLU. As a result, HLE provides a clear measurement of the gap between current AI capabilities and human expertise on closed-ended academic tasks, complementing other assessments of advanced capabilities in open-ended domains [[36](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib36), [10](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib10), [55](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib55), [35](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib35)].  
然而，当前最先进的模型在许多现有评估中已能取得近乎完美的分数[34, 49, 37, 16, 3, 56, 14]，这掩盖了当前及未来前沿人工智能能力的真实水平[38, 39, 27, 32]。因此，人们开始开发更具挑战性的基准测试，以检验多模态能力[10, 53, 48, 59, 2, 28, 31, 26, 57, 46]、强化现有基准[53, 48, 24, 45, 43]、通过多轮评审筛选问题[33, 30, 44, 18, 27]，并聘请专家编写测试高级学术知识的题目[44, 30, 18, 41, 34, 5]。HLE 综合了这些方法：题目由领域专家开发并经过多轮评审，同时保持了 MMLU 广泛的学科覆盖面。因此，HLE 清晰衡量了当前人工智能能力与人类专家在封闭式学术任务上的差距，补充了其他在开放式领域对高级能力的评估[36, 10, 55, 35]。

## 3Dataset  3 数据集

Humanity’s Last Exam (HLE) consists of 3,000 challenging questions across over a hundred subjects across. A high level summary is provided in [Figure˜3](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S1.F3 "In 1 Introduction ‣ Humanity’s Last Exam"). We publicly release these questions, while maintaining a private test set of held out questions to assess model overfitting.  
人类终极考试（HLE）包含 3,000 个具有挑战性的问题，涵盖一百多个学科领域。图˜3 提供了高级别概述。我们公开发布这些问题，同时保留一个私密的测试集，包含未公开的问题，以评估模型的过拟合情况。

### 3.1Collection  3.1 收集过程

HLE is a global collaborative effort, with questions from nearly 1000 subject expert contributors affiliated with over 500 institutions across 50 countries – comprised mostly of professors, researchers, and graduate degree holders.  
HLE 是一项全球协作努力，问题来自近 1000 名学科专家贡献者，他们隶属于 50 个国家的 500 多家机构——主要由教授、研究人员和研究生学位持有者组成。

##### Question Style.  问题风格。

HLE contains two question formats: exact-match questions (models provide an exact string as output) and multiple-choice questions (the model selects one of five or more answer choices). HLE is a multi-modal benchmark, with 10% of questions requiring comprehending both text and an image reference. 80% of questions are exact-match with the remainder being multiple-choice.  
HLE 包含两种题型：精确匹配题（模型需输出精确字符串）和多选题（模型从五个或更多选项中选择正确答案）。HLE 是一个多模态基准测试，其中 10%的题目需要同时理解文本和图像参考。80%的题目为精确匹配题，其余为多选题。

Each question submission includes several required components: the question text itself, answer specifications (either an an exact-match answer, or multiple-choice options with the correct answer marked), detailed rationale explaining the solution, academic subject, and contributor name and institutional affiliation to maintain accountability and accuracy.  
每道题目的提交需包含以下必要组成部分：题目文本本身、答案规范（精确匹配答案或标注正确答案的多选题选项）、详细解题思路、所属学科领域，以及贡献者姓名与所属机构以确保责任归属与答案准确性。

##### Submission Format.  提交格式。

To ensure question quality and integrity, we enforce strict submission criteria. Questions should be precise, unambiguous, solvable, and non-searchable, ensuring models cannot rely on memorization or simple retrieval methods. All submissions must be original work or non-trivial syntheses of published information, though contributions from unpublished research are acceptable. Questions typically require graduate-level expertise or test knowledge of highly specific topics (e.g., precise historical details, trivia, local customs) and have specific, unambiguous answers accepted by domain experts. When LLMs provide correct answers with faulty reasoning, authors are encouraged to modify question parameters, such as the number of answer choices, to discourage false positives. We require clear English with precise technical terminology, supporting LaTeX notation wherever necessary. Answers are kept short and easily verifiable for exact-match questions to support automatic grading. We prohibit open-ended questions, subjective interpretations, and content related to weapons of mass destruction. Finally, every question is accompanied by a detailed solution to verify accuracy.  
为确保问题质量与完整性，我们执行严格的提交标准。问题应精确、无歧义、可解答且不可搜索，确保模型无法依赖记忆或简单的检索方法。所有提交内容必须是原创作品或对已发表信息的非平凡综合，但未发表研究的贡献亦可接受。问题通常需要研究生水平的专业知识或测试高度特定主题的知识（例如精确的历史细节、冷门知识、地方习俗），并具有领域专家认可的明确、无歧义的答案。当 LLMs 提供正确但推理有误的答案时，鼓励作者修改问题参数（如选项数量）以减少误判。我们要求使用清晰英语及精确技术术语，必要时支持 LTX 符号标注。对于精确匹配类问题，答案应保持简短且易于验证，以支持自动评分。我们禁止开放式问题、主观解读以及与大规模杀伤性武器相关的内容。最后，每个问题都附有详细解答以验证准确性。

##### Prize Pool.  奖金池。

To attract high-quality submissions, we establish a $500,000 USD prize pool, with prizes of $5,000 USD for each of the top 50 questions and $500 USD for each of the next 500 questions, as determined by organizers. This incentive structure, combined with the opportunity for paper co-authorship for anyone with an accepted question in HLE, draws participation from qualified experts, particularly those with advanced degrees or significant technical experience in their fields.  
为吸引高质量投稿，我们设立了 500,000 美元的奖金池，其中前 50 名问题各奖励 5,000 美元，后续 500 名问题各奖励 500 美元，具体由组织者评定。这一激励措施，加上任何在 HLE 中被采纳的问题作者均有机会成为论文合著者，吸引了合格专家的参与，尤其是那些拥有高等学位或在其领域具备重要技术经验的人士。

### 3.2Review  3.2 评审

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2501.14249/assets/x4.png)

Figure 4:Dataset creation pipeline. We accept questions that make frontier LLMs fail, then iteratively refine them with the help of expert peer reviewers. Each question is then manually approved by organizers or expert reviewers trained by organizers. A private held-out set is kept in addition to the public set to assess model overfitting and gaming on the public benchmark.  
图 4：数据集创建流程。我们筛选出前沿 LLMs 无法回答的问题，随后在专家同行评审员的协助下进行迭代优化。每个问题最终需由组织者或经组织者培训的专家评审员手动审核通过。除公开数据集外，我们还保留一个私有隔离集，用于评估模型在公开基准测试中的过拟合与针对性优化现象。

##### LLM Difficulty Check  LLM 难度检查

To ensure question difficulty, each question is first validated against several frontier LLMs prior to submission ([Section˜B.1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A2.SS1 "B.1 Submission Process ‣ Appendix B Dataset ‣ Humanity’s Last Exam")). If the LLMs cannot solve the question (or in the case of multiple choices, if the models on average do worse than random guessing), the question proceeds to the next stage: human expert review. In total, we logged over 70,000 attempts, resulting in approximately 13,000 questions which stumped LLMs that were forwarded to expert human review.  
为确保题目难度，每道题目在提交前都会先经过多个前沿 LLMs 的验证（见第 B.1 节）。如果 LLMs 无法解答该题目（或在多项选择题中，若模型平均表现差于随机猜测），则该题目进入下一阶段：人类专家评审。我们总计记录了超过 70,000 次尝试，最终筛选出约 13,000 道难倒 LLMs 的题目，并提交给人类专家进行评审。

##### Expert Review  专家评审

Our human reviewers possess a graduate degree (eg. Master’s, PhD, JD, etc.) in their fields. Reviewers select submissions in their domain, grading them against standardized rubrics and offering feedback when applicable. There are two rounds of reviews. The first round focuses on iteratively refining submissions, with each question receiving between 1-3 reviews. In the second round, good and outstanding questions from the first round are identified and approved by organizers and reviewers to be included in the final HLE dataset. Details, instructions, and rubrics for both rounds can be found in [Section˜B.2](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A2.SS2 "B.2 Human Review Instructions ‣ Appendix B Dataset ‣ Humanity’s Last Exam"). [Figure˜4](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S3.F4 "In 3.2 Review ‣ 3 Dataset ‣ Humanity’s Last Exam") details our full process.  
我们的人类评审员均拥有其所在领域的硕士或博士学位（例如硕士、博士、法学博士等）。评审员选择其专业领域内的提交内容，依据标准化评分标准进行评分，并在适用时提供反馈。评审共进行两轮。第一轮侧重于迭代完善提交内容，每个问题会收到 1 至 3 份评审意见。在第二轮中，组织者和评审员会识别并批准第一轮中的优秀和杰出问题，将其纳入最终的 HLE 数据集。两轮评审的详细说明、指导原则和评分标准可在第˜B.2 节中找到。图˜4 详细展示了我们的完整流程。

Due to the advanced, specialized nature of many submissions, reviewers were not expected to verify the full accuracy of each provided solution rationale if it would take more than five minutes, instead focusing on whether the question aligns with guidelines. Given this limitation in the review process, we welcome community feedback. After initial release, we plan to conduct a public feedback period and periodically update the dataset, assessing any points of concern from the research community.  
由于许多提交内容具有高度专业性和复杂性，评审员无需花费超过五分钟来验证每个提供的解题思路的完全准确性，而是侧重于问题是否符合指导原则。考虑到评审过程中的这一限制，我们欢迎社区反馈。在初步发布后，我们计划开展公开反馈期，并定期更新数据集，评估研究界提出的任何关切点。

## 4Evaluation  4 评估

We evaluate the performance of state-of-the-art LLMs on HLE and analyze their capabilities across different question types and domains. We describe our evaluation setup ([Section˜4.1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4.SS1 "4.1 Setup ‣ 4 Evaluation ‣ Humanity’s Last Exam")) and present several quantitative results on metrics that track model performance ([Section˜4.2](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4.SS2 "4.2 Quantitative Results ‣ 4 Evaluation ‣ Humanity’s Last Exam")).  
我们评估了前沿 LLMs 在 HLE 上的表现，并分析了它们在不同题型和领域的能力。我们描述了评估设置（第 4.1 节），并展示了跟踪模型性能指标的若干定量结果（第 4.2 节）。

### 4.1Setup  4.1 设置

After data collection and review, we evaluated our final HLE dataset on additional frontier multi-modal LLMs. We employ a standardized system prompt that structures model responses into explicit reasoning followed by a final answer. As the question-answers are precise and close-ended, we use GPT-4o as a judge to verify answer correctness against model predictions while accounting for equivalent formats (e.g., decimals vs. fractions or estimations). Evaluation prompts are detailed in [Section˜C.1.1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS1.SSS1 "C.1.1 Evaluation ‣ C.1 Prompts ‣ Appendix C Evaluation ‣ Humanity’s Last Exam"), and exact model versions are provided in [Section˜C.4](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS4 "C.4 Model Versions ‣ Appendix C Evaluation ‣ Humanity’s Last Exam").  
在数据收集与审核后，我们在额外的前沿多模态 LLMs 上评估了最终的 HLE 数据集。我们采用标准化的系统提示，将模型响应结构化为明确的推理过程，后接最终答案。由于问题答案具有精确性和封闭性，我们使用 GPT-4o 作为评判者，根据模型预测验证答案正确性，同时考虑等效格式（例如小数与分数或估算值）。评估提示的详细信息见第 C.1.1 节，具体模型版本见第 C.4 节。

### 4.2Quantitative Results  4.2 定量结果

##### Accuracy.  准确性。

All frontier models achieve low accuracy on HLE ([Table˜1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4.T1 "In Calibration Error. ‣ 4.2 Quantitative Results ‣ 4 Evaluation ‣ Humanity’s Last Exam")), highlighting significant room for improvement in narrowing the gap between current LLMs and expert-level academic capabilities on closed-ended questions. These low scores are partially by design – the dataset collection process ([Section˜3.1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S3.SS1 "3.1 Collection ‣ 3 Dataset ‣ Humanity’s Last Exam")) attempts to filter out questions that existing models can answer correctly. Nevertheless, we notice upon evaluation, models exhibit non-zero accuracy. This is due to inherent noise in model inference – models can inconsistently guess the right answer or guess worse than random chance for multiple choice questions. We choose to leave these questions in the dataset as a natural component instead of strongly adversarially filtering. However, we stress the true capability floor of frontier models on the dataset will remain an open question and small inflections close to zero accuracy are not strongly indicative of progress.  
所有前沿模型在 HLE 上的准确率都很低（表˜1），这表明在封闭式问题上，当前 LLMs 与专家级学术能力之间仍有显著差距，存在很大的改进空间。这些低分部分是由于设计所致——数据集收集过程（第˜3.1 节）试图过滤掉现有模型能够正确回答的问题。尽管如此，我们在评估时注意到，模型表现出非零的准确率。这是由于模型推理中固有的噪声——模型可能会不一致地猜对答案，或者在多项选择题中猜得比随机机会更差。我们选择将这些问题保留在数据集中，作为自然组成部分，而不是进行强烈的对抗性过滤。然而，我们强调，前沿模型在该数据集上的真实能力下限仍是一个悬而未决的问题，接近零准确率的微小波动并不能强烈指示进展。

##### Calibration Error.  校准误差。

Given low performance on HLE, models should be calibrated, recognizing their uncertainty rather than confidently provide incorrect answers, indicative of confabulation/hallucination. To measure calibration, we prompt models to provide both an answer and their confidence from 0% to 100% ([Section˜C.1.1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS1.SSS1 "C.1.1 Evaluation ‣ C.1 Prompts ‣ Appendix C Evaluation ‣ Humanity’s Last Exam")), employing the setup from Wei et al. [[54](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib54)]. The implementation of our RMS calibration error is from Hendrycks et al. [[23](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib23)]. A well-calibrated model’s stated confidence should match its actual accuracy – for example, achieving 50% accuracy on questions where it claims 50% confidence. [Table˜1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4.T1 "In Calibration Error. ‣ 4.2 Quantitative Results ‣ 4 Evaluation ‣ Humanity’s Last Exam") reveals poor calibration across all models, reflected in high RMS calibration error scores. Models frequently provide incorrect answers with high confidence on HLE, failing to recognize when questions exceed their capabilities.  
鉴于在 HLE 上的低性能表现，模型应进行校准，认识到其不确定性，而非自信地提供错误答案，这显示出虚构/幻觉的迹象。为衡量校准程度，我们提示模型同时提供答案及其从 0%到 100%的置信度（第 C.1.1 节），采用了 Wei 等人[54]的设置。我们的 RMS 校准误差实现基于 Hendrycks 等人[23]的方法。一个良好校准的模型所声明的置信度应与其实际准确率相匹配——例如，在声称 50%置信度的问题上达到 50%的准确率。表 1 显示所有模型的校准效果均不佳，体现在较高的 RMS 校准误差分数上。模型在 HLE 上经常以高置信度提供错误答案，未能识别出问题超出其能力范围的情况。

|Model|Accuracy (%) ↑  准确率 (%) ↑|Calibration Error (%) ↓  <br>校准误差（%） ↓|
|---|---|---|
|GPT-4o|3.3|92.5|
|Grok 2|3.8|93.2|
|Claude 3.5 Sonnet|4.3|88.9|
|Gemini 1.5 Pro  双子座 1.5 Pro|5.0|93.1|
|Gemini 2.0 Flash Thinking  <br>双子座 2.0 闪电思维|6.2|93.9|
|o1|9.1|93.4|
|DeepSeek-R1∗  深度求索-R1 ∗|9.4|81.8|

Table 1:Accuracy and RMS calibration error of different models on HLE, demonstrating low accuracy and high calibration error across all models, indicative of hallucination. ∗Model is not multi-modal, evaluated on text-only subset. We report text-only results on all models in [Section˜C.2](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS2 "C.2 Text-Only Results ‣ Appendix C Evaluation ‣ Humanity’s Last Exam").  
表 1：不同模型在 HLE 上的准确率和 RMS 校准误差，显示所有模型均呈现低准确率和高校准误差，表明存在幻觉现象。 ∗ 该模型非多模态，仅在纯文本子集上评估。我们在第 C.2 节报告了所有模型的纯文本结果。

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2501.14249/assets/x5.png)

Figure 5:Average completion token counts of reasoning models tested, including both reasoning and output tokens. We also plot average token counts for non-reasoning models in [Section˜C.3](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS3 "C.3 Non-Reasoning Model Token Counts ‣ Appendix C Evaluation ‣ Humanity’s Last Exam").  
图 5：测试推理模型的平均完成标记数统计，包含推理标记和输出标记。非推理模型的平均标记数统计见第 C.3 节。

##### Token Counts.  标记数量分析。

Models with reasoning require substantially more inference time compute. To shed light on this in our evaluation, we analyze the number of completion tokens used across models. As shown in [Figure˜5](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4.F5 "In Calibration Error. ‣ 4.2 Quantitative Results ‣ 4 Evaluation ‣ Humanity’s Last Exam"), all reasoning models require generating significantly more tokens compared to non-reasoning models for an improvement in performance ([Section˜C.3](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS3 "C.3 Non-Reasoning Model Token Counts ‣ Appendix C Evaluation ‣ Humanity’s Last Exam")). We emphasize that future models should not only do better in terms of accuracy, but also strive to be compute-optimal.  
具备推理能力的模型需要显著更多的推理计算时间。为阐明此现象，我们分析了各模型使用的完成标记数量。如图 5 所示，所有推理模型为提升性能所需生成的标记数均远超非推理模型（详见第 C.3 节）。我们强调，未来模型不仅应在准确率上有所突破，更应致力于实现计算效率的最优化。

## 5Discussion  5 讨论

##### Future Model Performance.  
未来模型表现。

While current LLMs achieve very low accuracy on HLE, recent history shows benchmarks are quickly saturated – with models dramatically progressing from near-zero to near-perfect performance in a short timeframe [[44](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib44), [12](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib12)]. Given the rapid pace of AI development, it is plausible that models could exceed 50% accuracy on HLE by the end of 2025. High accuracy on HLE would demonstrate expert-level performance on closed-ended, verifiable questions and cutting-edge scientific knowledge, but it would not alone suggest autonomous research capabilities or “artificial general intelligence.” HLE tests structured academic problems rather than open-ended research or creative problem-solving abilities, making it a focused measure of technical knowledge and reasoning. HLE may be the last academic exam we need to give to models, but it is far from the last benchmark for AI.  
尽管当前 LLMs 在 HLE 上准确率极低，但近期历史表明基准测试往往被迅速攻克——模型在短时间内就能实现从接近零到近乎完美的跨越式进步[44, 12]。鉴于人工智能发展的迅猛势头，到 2025 年底模型在 HLE 上突破 50%准确率是可能实现的。HLE 的高准确率将证明模型在封闭式可验证问题与前沿科学知识方面已达到专家水平，但这本身并不意味其具备自主研究能力或"通用人工智能"。HLE 检测的是结构化学术问题，而非开放式研究或创造性解决问题的能力，这使其成为衡量技术知识与推理能力的聚焦标尺。HLE 或许是我们需要给模型的最后一场学术考试，但这远非人工智能的终极基准。

##### Impact.  影响。

By providing a clear measure of AI progress, HLE creates a common reference point for scientists and policymakers to assess AI capabilities. This enables more informed discussions about development trajectories, potential risks, and necessary governance measures.  
通过提供衡量人工智能进展的明确标准，人类终极考试为科学家和政策制定者评估人工智能能力建立了共同参照系。这有助于就发展路径、潜在风险及必要治理措施展开更具信息依据的讨论。

## References

- Alberti et al. [2019]C. Alberti, K. Lee, and M. Collins.A bert baseline for the natural questions, 2019.URL [https://arxiv.org/abs/1901.08634](https://arxiv.org/abs/1901.08634).
- Andriushchenko et al. [2024]M. Andriushchenko, A. Souly, M. Dziemian, D. Duenas, M. Lin, J. Wang, D. Hendrycks, A. Zou, Z. Kolter, M. Fredrikson, E. Winsor, J. Wynne, Y. Gal, and X. Davies.Agentharm: A benchmark for measuring harmfulness of llm agents, 2024.URL [https://arxiv.org/abs/2410.09024](https://arxiv.org/abs/2410.09024).
- Anthropic [2024a]Anthropic.The claude 3 model family: Opus, sonnet, haiku, 2024a.URL [https://api.semanticscholar.org/CorpusID:268232499](https://api.semanticscholar.org/CorpusID:268232499).
- Anthropic [2024b]Anthropic.Model card addendum: Claude 3.5 haiku and upgraded claude 3.5 sonnet, 2024b.URL [https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf).
- Anthropic [2024c]Anthropic.Responsible scaling policy updates, 2024c.URL [https://www.anthropic.com/rsp-updates](https://www.anthropic.com/rsp-updates).
- Austin et al. [2021]J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, and C. Sutton.Program synthesis with large language models, 2021.URL [https://arxiv.org/abs/2108.07732](https://arxiv.org/abs/2108.07732).
- Bai et al. [2022]Y. Bai, A. Jones, K. Ndousse, A. Askell, A. Chen, N. DasSarma, D. Drain, S. Fort, D. Ganguli, T. Henighan, N. Joseph, S. Kadavath, J. Kernion, T. Conerly, S. El-Showk, N. Elhage, Z. Hatfield-Dodds, D. Hernandez, T. Hume, S. Johnston, S. Kravec, L. Lovitt, N. Nanda, C. Olsson, D. Amodei, T. Brown, J. Clark, S. McCandlish, C. Olah, B. Mann, and J. Kaplan.Training a helpful and harmless assistant with reinforcement learning from human feedback, 2022.URL [https://arxiv.org/abs/2204.05862](https://arxiv.org/abs/2204.05862).
- Bajaj et al. [2018]P. Bajaj, D. Campos, N. Craswell, L. Deng, J. Gao, X. Liu, R. Majumder, A. McNamara, B. Mitra, T. Nguyen, M. Rosenberg, X. Song, A. Stoica, S. Tiwary, and T. Wang.Ms marco: A human generated machine reading comprehension dataset, 2018.URL [https://arxiv.org/abs/1611.09268](https://arxiv.org/abs/1611.09268).
- Bhatt et al. [2023]M. Bhatt, S. Chennabasappa, C. Nikolaidis, S. Wan, I. Evtimov, D. Gabi, D. Song, F. Ahmad, C. Aschermann, L. Fontana, S. Frolov, R. P. Giri, D. Kapil, Y. Kozyrakis, D. LeBlanc, J. Milazzo, A. Straumann, G. Synnaeve, V. Vontimitta, S. Whitman, and J. Saxe.Purple llama cyberseceval: A secure coding benchmark for language models, 2023.URL [https://arxiv.org/abs/2312.04724](https://arxiv.org/abs/2312.04724).
- Chan et al. [2024]J. S. Chan, N. Chowdhury, O. Jaffe, J. Aung, D. Sherburn, E. Mays, G. Starace, K. Liu, L. Maksin, T. Patwardhan, L. Weng, and A. Mądry.Mle-bench: Evaluating machine learning agents on machine learning engineering, 2024.URL [https://arxiv.org/abs/2410.07095](https://arxiv.org/abs/2410.07095).
- Chen et al. [2021]M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba.Evaluating large language models trained on code, 2021.URL [https://arxiv.org/abs/2107.03374](https://arxiv.org/abs/2107.03374).
- Chollet et al. [2024]F. Chollet, M. Knoop, G. Kamradt, and B. Landers.Arc prize 2024: Technical report, 2024.URL [https://arxiv.org/abs/2412.04604](https://arxiv.org/abs/2412.04604).
- Cobbe et al. [2021]K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman.Training verifiers to solve math word problems, 2021.URL [https://arxiv.org/abs/2110.14168](https://arxiv.org/abs/2110.14168).
- DeepSeek-AI [2024]DeepSeek-AI.Deepseek-v3 technical report, 2024.URL [https://github.com/deepseek-ai/DeepSeek-V3/blob/main/DeepSeek_V3.pdf](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/DeepSeek_V3.pdf).
- Dua et al. [2019]D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, and M. Gardner.Drop: A reading comprehension benchmark requiring discrete reasoning over paragraphs, 2019.URL [https://arxiv.org/abs/1903.00161](https://arxiv.org/abs/1903.00161).
- Dubey et al. [2024]A. Dubey et al.The llama 3 herd of models, 2024.URL [https://arxiv.org/abs/2407.21783](https://arxiv.org/abs/2407.21783).
- Gao et al. [2024]B. Gao, F. Song, Z. Yang, Z. Cai, Y. Miao, Q. Dong, L. Li, C. Ma, L. Chen, R. Xu, Z. Tang, B. Wang, D. Zan, S. Quan, G. Zhang, L. Sha, Y. Zhang, X. Ren, T. Liu, and B. Chang.Omni-math: A universal olympiad level mathematic benchmark for large language models, 2024.URL [https://arxiv.org/abs/2410.07985](https://arxiv.org/abs/2410.07985).
- Glazer et al. [2024]E. Glazer, E. Erdil, T. Besiroglu, D. Chicharro, E. Chen, A. Gunning, C. F. Olsson, J.-S. Denain, A. Ho, E. de Oliveira Santos, O. Järviniemi, M. Barnett, R. Sandler, J. Sevilla, Q. Ren, E. Pratt, L. Levine, G. Barkley, N. Stewart, B. Grechuk, T. Grechuk, and S. V. Enugandla.Frontiermath: A benchmark for evaluating advanced mathematical reasoning in ai, 2024.URL [https://arxiv.org/abs/2411.04872](https://arxiv.org/abs/2411.04872).
- He et al. [2024]C. He, R. Luo, Y. Bai, S. Hu, Z. L. Thai, J. Shen, J. Hu, X. Han, Y. Huang, Y. Zhang, J. Liu, L. Qi, Z. Liu, and M. Sun.Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024.URL [https://arxiv.org/abs/2402.14008](https://arxiv.org/abs/2402.14008).
- Hendrycks et al. [2021a]D. Hendrycks, S. Basart, S. Kadavath, M. Mazeika, A. Arora, E. Guo, C. Burns, S. Puranik, H. He, D. Song, and J. Steinhardt.Measuring coding challenge competence with apps, 2021a.URL [https://arxiv.org/abs/2105.09938](https://arxiv.org/abs/2105.09938).
- Hendrycks et al. [2021b]D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt.Measuring massive multitask language understanding, 2021b.URL [https://arxiv.org/abs/2009.03300](https://arxiv.org/abs/2009.03300).
- Hendrycks et al. [2021c]D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt.Measuring mathematical problem solving with the math dataset, 2021c.URL [https://arxiv.org/abs/2103.03874](https://arxiv.org/abs/2103.03874).
- Hendrycks et al. [2022]D. Hendrycks, A. Zou, M. Mazeika, L. Tang, B. Li, D. Song, and J. Steinhardt.Pixmix: Dreamlike pictures comprehensively improve safety measures, 2022.URL [https://arxiv.org/abs/2112.05135](https://arxiv.org/abs/2112.05135).
- Hosseini et al. [2024]A. Hosseini, A. Sordoni, D. Toyama, A. Courville, and R. Agarwal.Not all llm reasoners are created equal, 2024.URL [https://arxiv.org/abs/2410.01748](https://arxiv.org/abs/2410.01748).
- Jacovi et al. [2024]A. Jacovi, A. Wang, C. Alberti, C. Tao, J. Lipovetz, K. Olszewska, L. Haas, M. Liu, N. Keating, A. Bloniarz, C. Saroufim, C. Fry, D. Marcus, D. Kukliansky, G. S. Tomar, J. Swirhun, J. Xing, L. W. andMadhu Gurumurthy, M. Aaron, M. Ambar, R. Fellinger, R. Wang, R. Sims, Z. Zhang, S. Goldshtein, and D. Das.Facts leaderboard.[https://kaggle.com/facts-leaderboard](https://kaggle.com/facts-leaderboard), 2024.Google DeepMind, Google Research, Google Cloud, Kaggle.
- Jimenez et al. [2024]C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan.Swe-bench: Can language models resolve real-world github issues?, 2024.URL [https://arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770).
- Kiela et al. [2021]D. Kiela, M. Bartolo, Y. Nie, D. Kaushik, A. Geiger, Z. Wu, B. Vidgen, G. Prasad, A. Singh, P. Ringshia, Z. Ma, T. Thrush, S. Riedel, Z. Waseem, P. Stenetorp, R. Jia, M. Bansal, C. Potts, and A. Williams.Dynabench: Rethinking benchmarking in nlp, 2021.URL [https://arxiv.org/abs/2104.14337](https://arxiv.org/abs/2104.14337).
- Kumar et al. [2024]P. Kumar, E. Lau, S. Vijayakumar, T. Trinh, S. R. Team, E. Chang, V. Robinson, S. Hendryx, S. Zhou, M. Fredrikson, S. Yue, and Z. Wang.Refusal-trained llms are easily jailbroken as browser agents, 2024.URL [https://arxiv.org/abs/2410.13886](https://arxiv.org/abs/2410.13886).
- Laurent et al. [2024]J. M. Laurent, J. D. Janizek, M. Ruzo, M. M. Hinks, M. J. Hammerling, S. Narayanan, M. Ponnapati, A. D. White, and S. G. Rodriques.Lab-bench: Measuring capabilities of language models for biology research, 2024.URL [https://arxiv.org/abs/2407.10362](https://arxiv.org/abs/2407.10362).
- Li et al. [2024]N. Li, A. Pan, A. Gopal, S. Yue, D. Berrios, A. Gatti, J. D. Li, A.-K. Dombrowski, S. Goel, L. Phan, G. Mukobi, N. Helm-Burger, R. Lababidi, L. Justen, A. B. Liu, M. Chen, I. Barrass, O. Zhang, X. Zhu, R. Tamirisa, B. Bharathi, A. Khoja, Z. Zhao, A. Herbert-Voss, C. B. Breuer, S. Marks, O. Patel, A. Zou, M. Mazeika, Z. Wang, P. Oswal, W. Lin, A. A. Hunt, J. Tienken-Harder, K. Y. Shih, K. Talley, J. Guan, R. Kaplan, I. Steneker, D. Campbell, B. Jokubaitis, A. Levinson, J. Wang, W. Qian, K. K. Karmakar, S. Basart, S. Fitz, M. Levine, P. Kumaraguru, U. Tupakula, V. Varadharajan, R. Wang, Y. Shoshitaishvili, J. Ba, K. M. Esvelt, A. Wang, and D. Hendrycks.The wmdp benchmark: Measuring and reducing malicious use with unlearning, 2024.URL [https://arxiv.org/abs/2403.03218](https://arxiv.org/abs/2403.03218).
- Lu et al. [2024]P. Lu, H. Bansal, T. Xia, J. Liu, C. Li, H. Hajishirzi, H. Cheng, K.-W. Chang, M. Galley, and J. Gao.Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts, 2024.URL [https://arxiv.org/abs/2310.02255](https://arxiv.org/abs/2310.02255).
- McIntosh et al. [2024]T. R. McIntosh, T. Susnjak, N. Arachchilage, T. Liu, P. Watters, and M. N. Halgamuge.Inadequacies of large language model benchmarks in the era of generative artificial intelligence, 2024.URL [https://arxiv.org/abs/2402.09880](https://arxiv.org/abs/2402.09880).
- Nie et al. [2020]Y. Nie, A. Williams, E. Dinan, M. Bansal, J. Weston, and D. Kiela.Adversarial nli: A new benchmark for natural language understanding, 2020.URL [https://arxiv.org/abs/1910.14599](https://arxiv.org/abs/1910.14599).
- OpenAI [2024a]OpenAI.Openai o1 system card, 2024a.URL [https://cdn.openai.com/o1-system-card-20240917.pdf](https://cdn.openai.com/o1-system-card-20240917.pdf).
- OpenAI [2024b]OpenAI.Openai and los alamos national laboratory announce bioscience research partnership, 2024b.URL [https://openai.com/index/openai-and-los-alamos-national-laboratory-work-together/](https://openai.com/index/openai-and-los-alamos-national-laboratory-work-together/).
- OpenAI [2024c]OpenAI.Introducing swe-bench verified, 2024c.URL [https://openai.com/index/introducing-swe-bench-verified/](https://openai.com/index/introducing-swe-bench-verified/).
- OpenAI et al. [2024]OpenAI et al.Gpt-4 technical report, 2024.URL [https://arxiv.org/abs/2303.08774](https://arxiv.org/abs/2303.08774).
- Ott et al. [2022]S. Ott, A. Barbosa-Silva, K. Blagec, J. Brauner, and M. Samwald.Mapping global dynamics of benchmark creation and saturation in artificial intelligence._Nature Communications_, 13(1):6793, 2022.
- Owen [2024]D. Owen.How predictable is language model benchmark performance?, 2024.URL [https://arxiv.org/abs/2401.04757](https://arxiv.org/abs/2401.04757).
- Perez et al. [2022]E. Perez, S. Ringer, K. Lukošiūtė, K. Nguyen, E. Chen, S. Heiner, C. Pettit, C. Olsson, S. Kundu, S. Kadavath, A. Jones, A. Chen, B. Mann, B. Israel, B. Seethor, C. McKinnon, C. Olah, D. Yan, D. Amodei, D. Amodei, D. Drain, D. Li, E. Tran-Johnson, G. Khundadze, J. Kernion, J. Landis, J. Kerr, J. Mueller, J. Hyun, J. Landau, K. Ndousse, L. Goldberg, L. Lovitt, M. Lucas, M. Sellitto, M. Zhang, N. Kingsland, N. Elhage, N. Joseph, N. Mercado, N. DasSarma, O. Rausch, R. Larson, S. McCandlish, S. Johnston, S. Kravec, S. El Showk, T. Lanham, T. Telleen-Lawton, T. Brown, T. Henighan, T. Hume, Y. Bai, Z. Hatfield-Dodds, J. Clark, S. R. Bowman, A. Askell, R. Grosse, D. Hernandez, D. Ganguli, E. Hubinger, N. Schiefer, and J. Kaplan.Discovering language model behaviors with model-written evaluations, 2022.URL [https://arxiv.org/abs/2212.09251](https://arxiv.org/abs/2212.09251).
- Phuong et al. [2024]M. Phuong, M. Aitchison, E. Catt, S. Cogan, A. Kaskasoli, V. Krakovna, D. Lindner, M. Rahtz, Y. Assael, S. Hodkinson, H. Howard, T. Lieberum, R. Kumar, M. A. Raad, A. Webson, L. Ho, S. Lin, S. Farquhar, M. Hutter, G. Deletang, A. Ruoss, S. El-Sayed, S. Brown, A. Dragan, R. Shah, A. Dafoe, and T. Shevlane.Evaluating frontier models for dangerous capabilities, 2024.URL [https://arxiv.org/abs/2403.13793](https://arxiv.org/abs/2403.13793).
- Rajpurkar et al. [2016]P. Rajpurkar, J. Zhang, K. Lopyrev, and P. Liang.Squad: 100,000+ questions for machine comprehension of text, 2016.URL [https://arxiv.org/abs/1606.05250](https://arxiv.org/abs/1606.05250).
- Rajpurkar et al. [2018]P. Rajpurkar, R. Jia, and P. Liang.Know what you don’t know: Unanswerable questions for squad, 2018.URL [https://arxiv.org/abs/1806.03822](https://arxiv.org/abs/1806.03822).
- Rein et al. [2023]D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman.Gpqa: A graduate-level google-proof q&a benchmark, 2023.URL [https://arxiv.org/abs/2311.12022](https://arxiv.org/abs/2311.12022).
- Singhal et al. [2023]K. Singhal, S. Azizi, T. Tu, S. S. Mahdavi, J. Wei, H. W. Chung, N. Scales, A. Tanwani, H. Cole-Lewis, S. Pfohl, et al.Large language models encode clinical knowledge._Nature_, 620(7972):172–180, 2023.
- Srinivasan et al. [2023]V. K. Srinivasan, Z. Dong, B. Zhu, B. Yu, H. Mao, D. Mosk-Aoyama, K. Keutzer, J. Jiao, and J. Zhang.Nexusraven: A commercially-permissive language model for function calling.In _NeurIPS 2023 Foundation Models for Decision Making Workshop_, 2023.URL [https://openreview.net/forum?id=5lcPe6DqfI](https://openreview.net/forum?id=5lcPe6DqfI).
- Srivastava et al. [2023]A. Srivastava, A. Rastogi, A. Rao, A. A. M. Shoeb, A. Abid, A. Fisch, A. R. Brown, A. Santoro, A. Gupta, A. Garriga-Alonso, A. Kluska, A. Lewkowycz, A. Agarwal, A. Power, A. Ray, A. Warstadt, A. W. Kocurek, A. Safaya, A. Tazarv, A. Xiang, A. Parrish, A. Nie, A. Hussain, A. Askell, A. Dsouza, A. Slone, A. Rahane, A. S. Iyer, A. Andreassen, A. Madotto, A. Santilli, A. Stuhlmüller, A. Dai, A. La, A. Lampinen, A. Zou, et al.Beyond the imitation game: Quantifying and extrapolating the capabilities of language models, 2023.URL [https://arxiv.org/abs/2206.04615](https://arxiv.org/abs/2206.04615).
- Taghanaki et al. [2024]S. A. Taghanaki, A. Khani, and A. Khasahmadi.Mmlu-pro+: Evaluating higher-order reasoning and shortcut learning in llms, 2024.URL [https://arxiv.org/abs/2409.02257](https://arxiv.org/abs/2409.02257).
- Team et al. [2024]G. Team et al.Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context, 2024.URL [https://arxiv.org/abs/2403.05530](https://arxiv.org/abs/2403.05530).
- Tsoukalas et al. [2024]G. Tsoukalas, J. Lee, J. Jennings, J. Xin, M. Ding, M. Jennings, A. Thakur, and S. Chaudhuri.Putnambench: Evaluating neural theorem-provers on the putnam mathematical competition, 2024.URL [https://arxiv.org/abs/2407.11214](https://arxiv.org/abs/2407.11214).
- Wang et al. [2019]A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman.Glue: A multi-task benchmark and analysis platform for natural language understanding, 2019.URL [https://arxiv.org/abs/1804.07461](https://arxiv.org/abs/1804.07461).
- Wang et al. [2020]A. Wang, Y. Pruksachatkun, N. Nangia, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman.Superglue: A stickier benchmark for general-purpose language understanding systems, 2020.URL [https://arxiv.org/abs/1905.00537](https://arxiv.org/abs/1905.00537).
- Wang et al. [2024]Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, T. Li, M. Ku, K. Wang, A. Zhuang, R. Fan, X. Yue, and W. Chen.Mmlu-pro: A more robust and challenging multi-task language understanding benchmark (published at neurips 2024 track datasets and benchmarks), 2024.URL [https://arxiv.org/abs/2406.01574](https://arxiv.org/abs/2406.01574).
- Wei et al. [2024]J. Wei, N. Karina, H. W. Chung, Y. J. Jiao, S. Papay, A. Glaese, J. Schulman, and W. Fedus.Measuring short-form factuality in large language models, 2024.URL [https://arxiv.org/abs/2411.04368](https://arxiv.org/abs/2411.04368).
- Wijk et al. [2024]H. Wijk, T. Lin, J. Becker, S. Jawhar, N. Parikh, T. Broadley, L. Chan, M. Chen, J. Clymer, J. Dhyani, E. Ericheva, K. Garcia, B. Goodrich, N. Jurkovic, M. Kinniment, A. Lajko, S. Nix, L. Sato, W. Saunders, M. Taran, B. West, and E. Barnes.Re-bench: Evaluating frontier ai r&d capabilities of language model agents against human experts, 2024.URL [https://arxiv.org/abs/2411.15114](https://arxiv.org/abs/2411.15114).
- xAI [2024]xAI.Grok-2 beta release, 2024.URL [https://x.ai/blog/grok-2](https://x.ai/blog/grok-2).
- Yan et al. [2024]F. Yan, H. Mao, C. C.-J. Ji, T. Zhang, S. G. Patil, I. Stoica, and J. E. Gonzalez.Berkeley function calling leaderboard.[https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html), 2024.
- Yang et al. [2018]Z. Yang, P. Qi, S. Zhang, Y. Bengio, W. W. Cohen, R. Salakhutdinov, and C. D. Manning.Hotpotqa: A dataset for diverse, explainable multi-hop question answering, 2018.URL [https://arxiv.org/abs/1809.09600](https://arxiv.org/abs/1809.09600).
- Yao et al. [2024]S. Yao, N. Shinn, P. Razavi, and K. Narasimhan.τ-bench: A benchmark for tool-agent-user interaction in real-world domains, 2024.URL [https://arxiv.org/abs/2406.12045](https://arxiv.org/abs/2406.12045).
- Zhang et al. [2024]A. K. Zhang, N. Perry, R. Dulepet, J. Ji, J. W. Lin, E. Jones, C. Menders, G. Hussein, S. Liu, D. Jasper, P. Peetathawatchai, A. Glenn, V. Sivashankar, D. Zamoshchin, L. Glikbarg, D. Askaryar, M. Yang, T. Zhang, R. Alluri, N. Tran, R. Sangpisit, P. Yiorkadjis, K. Osele, G. Raghupathi, D. Boneh, D. E. Ho, and P. Liang.Cybench: A framework for evaluating cybersecurity capabilities and risks of language models, 2024.URL [https://arxiv.org/abs/2408.08926](https://arxiv.org/abs/2408.08926).
- Zhong et al. [2023]W. Zhong, R. Cui, Y. Guo, Y. Liang, S. Lu, Y. Wang, A. Saied, W. Chen, and N. Duan.Agieval: A human-centric benchmark for evaluating foundation models, 2023.URL [https://arxiv.org/abs/2304.06364](https://arxiv.org/abs/2304.06364).

## Appendix AAuthors  附录 A 作者

We offered optional co-authorship to all question submitters with an accepted question in Humanity’s Last Exam (including both public and private splits). All potential co-authors with an accepted question were contacted directly. Authorship order is ranked based on the number of accepted questions in Humanity’s Last Exam.  
我们向所有在"人类终极考试"中提交并被采纳的问题提供者提供了可选的共同作者身份（包括公开和私密部分）。所有提交问题被采纳的潜在共同作者均已直接联系。作者顺序根据在"人类终极考试"中被采纳问题的数量进行排序。

As we give co-authors the time and freedom to choose between opting-in or staying anonymous, we will periodically update this list. We further note that this list only represents a subset of our participating institutions and authors, many chose to remain anonymous.  
在我们给予合著者时间和自由来选择是否署名或保持匿名期间，我们将定期更新这份名单。我们进一步说明，这份名单仅代表参与机构及作者中的一部分，许多人选择保持匿名。

### A.1Data Contributors & Affiliations  
A.1 数据贡献者与所属机构

In progress. Sorted in descending order by number of accepted questions.  
进行中。按已采纳问题数量降序排列。

Authors Daron Anderson3, Tung Nguyen4, Mobeen Mahmood5, Fiona Feng6, Steven Y. Feng7, Haoran Zhao8, Michael Yu3, Varun Gangal3, Chelsea Zou7, Zihan Wang9, Jessica P. Wang10, Pawan Kumar11, Oleksandr Pokutnyi12, Robert Gerbicz13, Serguei Popov14, John-Clark Levin15, Mstyslav Kazakov16, Johannes Schmitt17, Geoff Galgon18, Alvaro Sanchez3, Yongki Lee19, Will Yeadon20, Scott Sauers21, Marc Roth22, Chidozie Agu23, Søren Riis22, Fabian Giska3, Saiteja Utpala24, Zachary Giboney25, Gashaw M. Goshu3, Joan of Arc Xavier26, Sarah-Jane Crowson27, Mohinder Maheshbhai Naiya28, Noah Burns7, Lennart Finke17, Zerui Cheng29, Hyunwoo Park30, Francesco Fournier-Facio15, John Wydallis3, Mark Nandor3, Ankit Singh31, Tim Gehrunger17, Jiaqi Cai32, Ben McCarty33, Darling Duclosel34, Jungbae Nam35, Jennifer Zampese36, Ryan G. Hoerr37, Aras Bacho38, Gautier Abou Loume 39,40, Abdallah Galal41, Hangrui Cao30, Alexis C Garretson42,43, Damien Sileo44, Qiuyu Ren45, Doru Cojoc46, Pavel Arkhipov47, Usman Qazi48,49, Lianghui Li50, Sumeet Motwani51, Christian Schroeder de Witt51, Edwin Taylor3, Johannes Veith52,53, Eric Singer54, Taylor D. Hartman55, Paolo Rissone56, Jaehyeok Jin46, Jack Wei Lun Shi57, Chris G. Willcocks20, Joshua Robinson58, Aleksandar Mikov50, Ameya Prabhu59, Longke Tang29, Xavier Alapont26, Justine Leon Uro3, Kevin Zhou45, Emily de Oliveira Santos60, Andrey Pupasov Maksimov61, Edward Vendrow32, Kengo Zenitani3, Julien Guillod62,63, Yuqi Li64, Joshua Vendrow32, Vladyslav Kuchkin 65, Ng Ze-An66, Pierre Marion50, Denis Efremov67, Jayson Lynch32, Kaiqu Liang29, Andrew Gritsevskiy68, Dakotah Martinez3, Ben Pageler3, Nick Crispino69, Dimitri Zvonkine70,71, Natanael Wildner Fraga3, Saeed Soori72, Ori Press59, Henry Tang51, Julian Salazar73, Sean R. Green3, Lina Brüssel15, Moon Twayana74, Aymeric Dieuleveut75, T. Ryan Rogers76, Wenjin Zhang69, Bikun Li77, Jinzhou Yang78, Arun Rao79, Gabriel Loiseau44, Mikhail Kalinin80, Marco Lukas81, Ciprian Manolescu7, Subrata Mishra82, Ariel Ghislain Kemogne Kamdoum83, Tobias Kreiman45, Tad Hogg84, Alvin Jin32, Carlo Bosio45, Gongbo Sun85, Brian P Coppola86, Tim Tarver87, Haline Heidinger88,89, Rafael Sayous71, Stefan Ivanov15, Joseph M Cavanagh45, Jiawei Shen69, Joseph Marvin Imperial90,91, Philippe Schwaller50, Shaipranesh Senthilkuma50, Andres M Bran50, Ali Dehghan3, Andres Algaba92, Brecht Verbeken92, David Noever93, Ragavendran P V3, Lisa Schut51, Ilia Sucholutsky94, Evgenii Zheltonozhskii95, Derek Lim32, Richard Stanley32,96, Shankar Sivarajan 97, Tong Yang30, John Maar98, Julian Wykowski15, Martí Oller15, Jennifer Sandlin99, Anmol Sahu3, Yuzheng Hu100, Sara Fish101, Nasser Heydari3, Archimedes Apronti102, Kaivalya Rawal51, Tobias Garcia Vilchis103, Yuexuan Zu32, Martin Lackner104, James Koppel3, Jeremy Nguyen105, Daniil S. Antonenko106, Steffi Chern30, Bingchen Zhao107, Pierrot Arsene108, Alan Goldfarb45, Sergey Ivanov3, Rafał Poświata109, Chenguang Wang69, Daofeng Li69, Donato Crisostomi56, Andrea Achilleos110, Benjamin Myklebust111, Archan Sen45, David Perrella112, Nurdin Kaparov113, Mark H Inlow114, Allen Zang77, Elliott Thornley115, Daniil Orel116, Vladislav Poritski3, Shalev Ben-David117, Zachary Berger32, Parker Whitfill32, Michael Foster3, Daniel Munro9, Linh Ho3, Dan Bar Hava118, Aleksey Kuchkin3, Robert Lauff98, David Holmes119, Frank Sommerhage120, Keith Schneider3, Zakayo Kazibwe121, Nate Stambaugh122, Mukhwinder Singh123, Ilias Magoulas124, Don Clarke125, Dae Hyun Kim126, Felipe Meneguitti Dias60, Veit Elser127, Kanu Priya Agarwal3, Victor Efren Guadarrama Vilchis128, Immo Klose46, Christoph Demian53, Ujjwala Anantheswaran99, Adam Zweiger32, Guglielmo Albani129, Jeffery Li32, Nicolas Daans130, Maksim Radionov131, Václav Rozhoň132, Ziqiao Ma86, Christian Stump133, Mohammed Berkani134, Jacob Platnick135, Volodymyr Nevirkovets136, Luke Basler137, Marco Piccardo138, Ferenc Jeanplong139, Niv Cohen94, Josef Tkadlec140, Paul Rosu141, Piotr Padlewski3, Stanislaw Barzowski3, Kyle Montgomery69, Aline Menezes3, Arkil Patel5,142, Zixuan Wang29, Jamie Tucker-Foltz101, Jack Stade143, Tom Goertzen144, Fereshteh Kazemi3, Jeremiah Milbauer30, John Arnold Ambay145, Abhishek Shukla146, Yan Carlos Leyva Labrador26, Alan Givré147, Hew Wolff3, Vivien Rossbach 26, Muhammad Fayez Aziz100, Younesse Kaddar51, Yanxu Chen148, Robin Zhang32, Jiayi Pan45, Antonio Terpin17, Niklas Muennighoff7, Hailey Schoelkopf3, Eric Zheng30, Avishy Carmi149, Adam Jones3, Jainam Shah150, Ethan D. L. Brown151, Kelin Zhu97, Max Bartolo152, Richard Wheeler107, Andrew Ho153, Shaul Barkan154, Jiaqi Wang8, Martin Stehberger3, Egor Kretov155, Kaustubh Sridhar156, Zienab EL-Wasif157, Anji Zhang32, Daniel Pyda158, Joanna Tam159, David M. Cunningham160, Vladimir Goryachev3, Demosthenes Patramanis51, Michael Krause161, Andrew Redenti46, Daniel Bugas3, David Aldous45, Jesyin Lai162, Shannon Coleman49, Mohsen Bahaloo163, Jiangnan Xu164, Sangwon Lee3, Sandy Zhao26, Ning Tang45, Michael K. Cohen45, Micah Carroll45, Orr Paradise45, Jan Hendrik Kirchner165, Stefan Steinerberger8, Maksym Ovchynnikov166, Jason O. Matos159, Adithya Shenoy3, Benedito Alves de Oliveira Junior60, Michael Wang45, Yuzhou Nie167, Paolo Giordano168, Philipp Petersen168, Anna Sztyber-Betley169, Priti Shukla170, Jonathan Crozier171, Antonella Pinto172, Shreyas Verma173, Prashant Joshi174, Zheng-Xin Yong175, Allison Tee7, Jérémy Andréoletti63, Orion Weller176, Raghav Singhal116, Gang Zhang3, Alexander Ivanov177, Seri Khoury132, Hamid Mostaghimi83, Kunvar Thaman178, Qijia Chen101, Tran Quoc Khánh179, Jacob Loader15, Stefano Cavalleri180, Hannah Szlyk69, Zachary Brown32, Jonathan Roberts15, William Alley3, Kunyang Sun45, Ryan Stendall181, Max Lamparth7, Anka Reuel7, Ting Wang69, Hanmeng Xu106, Sreenivas Goud Raparthi182, Pablo Hernández-Cámara183, Freddie Martin3, Dmitry Malishev3, Thomas Preu184, Tomek Korbak185, Marcus Abramovitch3, Dominic Williamson144, Ziye Chen186, Biró Bálint3, M Saiful Bari187, Peyman Kassani188, Zihao Wang77, Behzad Ansarinejad3, Laxman Prasad Goswami146, Yewen Sun189, Hossam Elgnainy190, Daniel Tordera191, George Balabanian156, Earth Anderson192, Lynna Kvistad193, Alejandro José Moyano194, Rajat Maheshwari 195, Ahmad Sakor81, Murat Eron196, Isaac C. McAlister3, Javier Gimenez26, Innocent Enyekwe3, Andrew Favre D.O.197, Shailesh Shah198, Xiaoxiang Zhou53, Firuz Kamalov199, Ronald Clark51, Sherwin Abdoli172, Tim Santens15, Khalida Meer26, Harrison K Wang101, Kalyan Ramakrishnan51, Evan Chen32, Alessandro Tomasiello200, G. Bruno De Luca7, Shi-Zhuo Looi38, Vinh-Kha Le45, Noam Kolt154, Niels Mündler17, Avi Semler51, Emma Rodman201, Jacob Drori3, Carl J Fossum202, Milind Jagota45, Ronak Pradeep117, Honglu Fan203, Tej Shah204, Jonathan Eicher 205, Michael Chen38, Kushal Thaman7, William Merrill94, Carter Harris206, Jason Gross3, Ilya Gusev3, Asankhaya Sharma207, Shashank Agnihotri208, Pavel Zhelnov72, Siranut Usawasutsakorn209, Mohammadreza Mofayezi72, Sergei Bogdanov210, Alexander Piperski211, Marc Carauleanu212, David K. Zhang7, Dylan Ler3, Roman Leventov213, Ignat Soroko74, Thorben Jansen214, Pascal Lauer215,216, Joshua Duersch217, Vage Taamazyan218, Wiktor Morak3, Wenjie Ma45, William Held7,135, Tran Đuc Huy219, Ruicheng Xian100, Armel Randy Zebaze220, Mohanad Mohamed221, Julian Noah Leser104, Michelle X Yuan3, Laila Yacar222, Johannes Lengler17, Hossein Shahrtash223, Edson Oliveira224, Joseph W. Jackson225, Daniel Espinosa Gonzalez167, Andy Zou30,226, Muthu Chidambaram141, Timothy Manik3, Hector Haffenden3, Dashiell Stander227, Ali Dasouqi176, Alexander Shen228, Emilien Duc17, Bita Golshani3, David Stap148, Mikalai Uzhou229, Alina Borisovna Zhidkovskaya230, Lukas Lewark17, Mátyás Vincze231,232, Dustin Wehr3, Colin Tang30, Zaki Hossain233, Shaun Phillips3, Jiang Muzhen3, Fredrik Ekström3, Angela Hammon3, Oam Patel101, Nicolas Remy234, Faraz Farhidi235, George Medley 3, Forough Mohammadzadeh3, Madellene Peñaflor236, Haile Kassahun5, Alena Friedrich237, Claire Sparrow77, Taom Sakal167, Omkar Dhamane238, Ali Khajegili Mirabadi49, Eric Hallman3, Mike Battaglia3, Mohammad Maghsoudimehrabani239, Hieu Hoang240, Alon Amit241, Dave Hulbert3, Roberto Pereira242, Simon Weber17, Stephen Mensah243, Nathan Andre244, Anton Peristyy3, Chris Harjadi7, Himanshu Gupta 99, Stephen Malina245, Samuel Albanie3, Will Cai45, Mustafa Mehkary 72,246, Frank Reidegeld3, Anna-Katharina Dick59, Cary Friday247, Jasdeep Sidhu3, Wanyoung Kim248, Mariana Costa26, Hubeyb Gurdogan79, Brian Weber249, Harsh Kumar 250, Tong Jiang101, Arunim Agarwal251, Chiara Ceconello3, Warren S. Vaz3, Chao Zhuang3, Haon Park252,253, Andrew R. Tawfeek8, Daattavya Aggarwal15, Michael Kirchhof59, Linjie Dai32, Evan Kim32, Johan Ferret73, Yuzhou Wang135, Minghao Yan85, Krzysztof Burdzy8, Lixin Zhang26, Antonio Franca15, Diana T. Pham254, Kang Yong Loh7, Joshua Robinson255, Shreen Gul256, Gunjan Chhablani135, Zhehang Du156, Adrian Cosma257, Colin White258, Robin Riblet108, Prajvi Saxena259, Jacob Votava29, Vladimir Vinnikov3, Ethan Delaney260, Shiv Halasyamani261, Syed M. Shahid262, Jean-Christophe Mourrat70,263, Lavr Vetoshkin264, Renas Bacho265, Vincent Ginis92,101, Aleksandr Maksapetyan26, Florencia de la Rosa266, Xiuyu Li45, Guillaume Malod267, Leon Lang148, Julien Laurendeau50, Fatimah Adesanya 26,268, Julien Portier15, Lawrence Hollom15, Victor Souza15, Yuchen Anna Zhou269, Yiğit Yalın270, Gbenga Daniel Obikoya3, Luca Arnaboldi50, Rai (Michael Pokorny)271, Filippo Bigi50, Kaniuar Bacho107, Pierre Clavier272, Gabriel Recchia273, Mara Popescu274, Nikita Shulga275, Ngefor Mildred Tanwie 276, Thomas C.H. Lux277, Ben Rank3, Colin Ni79, Alesia Yakimchyk278, Huanxu (Quinn) Liu 279, Olle Häggström280, Emil Verkama281, Himanshu Narayan 3, Hans Gundlach32, Leonor Brito-Santana282, Brian Amaro7, Vivek Vajipey7, Rynaa Grover135, Yiyang Fan3, Gabriel Poesia Reis e Silva7, Linwei Xin77, Yosi Kratish136, Jakub Łucki17, Wen-Ding Li127, Justin Xu51, Kevin Joseph Scaria99, Freddie Vargus283, Farzad Habibi284, Long (Tony) Lian45, Emanuele Rodolà56, Jules Robins3, Vincent Cheng9, Declan Grabb7, Ida Bosio285, Tony Fruhauff3, Ido Akov286, Eve J. Y. Lo287, Hao Qi186, Xi Jiang77, Ben Segev46, Jingxuan Fan101, Sarah Martinson101, Erik Y. Wang101, Kaylie Hausknecht101, Michael P. Brenner101, Mao Mao186, Yibo Jiang77, Xinyu Zhang186, David Avagian208, Eshawn Jessica Scipio288, Muhammad Rehan Siddiqi289,290, Alon Ragoler291, Justin Tan15, Deepakkumar Patil292, Rebeka Plecnik3, Aaron Kirtland175, Roselynn Grace Montecillo293, Stephane Durand294, Omer Faruk Bodur3, Zahra Adoul295, Mohamed Zekry 296, Guillaume Douville26, Ali Karakoc297, Tania C. B. Santos3, Samir Shamseldeen298, Loukmane Karim246, Anna Liakhovitskaia299, Nate Resman 300, Nicholas Farina26, Juan Carlos Gonzalez301, Gabe Maayan186, Sarah Hoback101, Rodrigo De Oliveira Pena302, Glen Sherman26, Hodjat Mariji3, Rasoul Pouriamanesh3, Wentao Wu49, Gözdenur Demir3, Sandra Mendoza303,304, Ismail Alarab305, Joshua Cole306, Danyelle Ferreira26, Bryan Johnson 307, Hsiaoyun Milliron308, Mohammad Safdari309, Liangti Dai51, Siriphan Arthornthurasuk26, Alexey Pronin310, Jing Fan274, Angel Ramirez-Trinidad3, Ashley Cartwright311, Daphiny Pottmaier312, Omid Taheri313, David Outevsky314, Stanley Stepanic315, Samuel Perry3, Luke Askew316, Raúl Adrián Huerta Rodríguez 3, Abdelkader Dendane26, Sam Ali58, Ricardo Lorena317, Krishnamurthy Iyer318, Sk Md Salauddin319, Murat Islam320, Juan Gonzalez3, Josh Ducey321, Russell Campbell322, Maja Somrak3, Vasilios Mavroudis323, Eric Vergo3, Juehang Qin324, Benjámin Borbás325, Eric Chu73, Jack Lindsey165, Anil Radhakrishnan171, Antoine Jallon3, I.M.J. McInnis3, Alex Hoover77, Sören Möller326, Song Bian85, John Lai26, Tejal Patwardhan271  
作者：达伦·安德森 3 、Tung Nguyen 4 、莫宾·马哈茂德 5 、Fiona Feng 6 、Steven Y. Feng 7 、赵浩然 8 、Michael Yu 3 、瓦伦·甘加尔 3 、Chelsea Zou 7 、王梓涵 9 、Jessica P. Wang 10 、帕万·库马尔 11 、奥列克桑德尔·波库特尼 12 、罗伯特·格比茨 13 、谢尔盖·波波夫 14 、约翰-克拉克·莱文 15 、姆斯季斯拉夫·卡扎科夫 16 、约翰内斯·施密特 17 、杰夫·加尔贡 18 、阿尔瓦罗·桑切斯 3 、李容基 19 、威尔·伊登 20 、斯科特·索尔斯 21 、马克·罗斯 22 、奇多齐·阿古 23 、索伦·里斯 22 、法比安·吉斯卡 3 、赛特贾·乌特帕拉 24 、扎卡里·吉博尼 25 、加肖·M·戈舒 3 、圣女贞德·泽维尔 26 、莎拉-简·克劳森 27 、莫欣德·马赫什巴伊·奈亚 28 、诺亚·伯恩斯 7 、伦纳特·芬克 17 、程泽瑞 29 、朴贤宇 30 、弗朗切斯科·富尔尼耶-法西奥 15 、约翰·怀达利斯 3 、马克·南多尔 3 、安基特·辛格 31 、蒂姆·格伦格 17 、蔡佳琪 32 、本·麦卡蒂 33 、达林·杜克洛塞尔 34 、南正培 35 、詹妮弗·赞佩塞 36 、瑞安·G 霍尔 37 、阿拉斯·巴乔 38 、高蒂埃·阿布·卢姆 39,40 、阿卜杜拉·贾拉勒 41 、曹航瑞 30 、亚历克西斯·C·加勒特森 42,43 、达米安·西莱奥 44 、任秋雨 45 、多鲁·科约克 46 、帕维尔·阿尔希波夫 47 、乌斯曼·卡齐 48,49 、李良辉 50 、苏米特·莫特瓦尼 51 、克里斯蒂安·施罗德·德·维特 51 、埃德温·泰勒 3 、约翰内斯·法伊特 52,53 、埃里克·辛格 54 、泰勒·D·哈特曼 55 、保罗·里索内 56 、金宰赫 46 、施伟伦 57 、克里斯·G·威尔科克斯 20 、约书亚·罗宾逊 58 、亚历山大·米科夫 50 、阿梅亚·普拉布 59 、唐龙科 29 、泽维尔·阿拉蓬特 26 、贾斯汀·莱昂·乌罗 3 、周凯文 45 、艾米丽·德·奥利维拉·桑托斯 60 、安德烈·普帕索夫·马克西莫夫 61 、爱德华·文德罗 32 、善谷健吾 3 、朱利安·吉约 62,63 、李玉琪 64 、约书亚·文德罗 32 、弗拉迪斯拉夫·库奇金 65 、吴泽安 66 、皮埃尔·马里昂 50 、丹尼斯·叶夫列莫夫 67 、杰森·林奇 32 、梁凯渠 29 、安德鲁·格里采夫斯基 68 、达科塔·马丁内斯 3 、本·帕格勒 3 、尼克·克里斯皮诺 69 、迪米特里·兹冯金 70,71 、纳塔内尔·维尔德纳·弗拉加 3 、赛义德·苏里 72 、奥里·普雷斯 59 、唐亨利 51 、朱利安·萨拉查 73 、肖恩·R· 格林 3 ，莉娜·布鲁塞尔 15 ，穆恩·特瓦亚纳 74 ，艾默里克·迪厄勒沃 75 ，T. Ryan Rogers 76 , Wenjin Zhang 69 , Bikun Li 77 , Jinzhou Yang 78 , Arun Rao 79 , Gabriel Loiseau 44 , Mikhail Kalinin 80 , Marco Lukas 81 , Ciprian Manolescu 7 , Subrata Mishra 82 , Ariel Ghislain Kemogne Kamdoum 83 , Tobias Kreiman 45 , Tad Hogg 84 , Alvin Jin 32 , Carlo Bosio 45 , Gongbo Sun 85 , Brian P Coppola 86 , Tim Tarver 87 , Haline Heidinger 88,89 , Rafael Sayous 71 , Stefan Ivanov 15 , Joseph M Cavanagh 45 , Jiawei Shen 69 , Joseph Marvin Imperial 90,91 , Philippe Schwaller 50 , Shaipranesh Senthilkuma 50 , Andres M Bran 50 , Ali Dehghan 3 , Andres Algaba 92 , Brecht Verbeken 92 , David Noever 93 , Ragavendran P V 3 , Lisa Schut 51 , Ilia Sucholutsky 94 , Evgenii Zheltonozhskii 95 , Derek Lim 32 , Richard Stanley 32,96 , Shankar Sivarajan 97 , Tong Yang 30 , John Maar 98 , Julian Wykowski 15 , Martí Oller 15 , Jennifer Sandlin 99 , Anmol Sahu 3 , Yuzheng Hu 100 , Sara Fish 101 , Nasser Heydari 3 , Archimedes Apronti 102 , Kaivalya Rawal 51 , Tobias Garcia Vilchis 103 , Yuexuan Zu 32 , Martin Lackner 104 , James Koppel 3 , 杰里米·阮 105 ，丹尼尔·S。 Antonenko 106 , Steffi Chern 30 , Bingchen Zhao 107 , Pierrot Arsene 108 , Alan Goldfarb 45 , Sergey Ivanov 3 , Rafał Poświata 109 , Chenguang Wang 69 , Daofeng Li 69 , Donato Crisostomi 56 , Andrea Achilleos 110 , Benjamin Myklebust 111 , Archan Sen 45 , David Perrella 112 , Nurdin Kaparov 113 , Mark H Inlow 114 , Allen Zang 77 , Elliott Thornley 115 , Daniil Orel 116 , Vladislav Poritski 3 , Shalev Ben-David 117 , Zachary Berger 32 , Parker Whitfill 32 , Michael Foster 3 , Daniel Munro 9 , Linh Ho 3 , Dan Bar Hava 118 , Aleksey Kuchkin 3 , Robert Lauff 98 , David Holmes 119 , Frank Sommerhage 120 , Keith Schneider 3 , Zakayo Kazibwe 121 , Nate Stambaugh 122 , Mukhwinder Singh 123 , Ilias Magoulas 124 , Don Clarke 125 , Dae Hyun Kim 126 , Felipe Meneguitti Dias 60 , Veit Elser 127 , Kanu Priya Agarwal 3 , Victor Efren Guadarrama Vilchis 128 , Immo Klose 46 , Christoph Demian 53 , Ujjwala Anantheswaran 99 , Adam Zweiger 32 , Guglielmo Albani 129 , Jeffery Li 32 , Nicolas Daans 130 , Maksim Radionov 131 , Václav Rozhoň 132 , Ziqiao Ma 86 , 克里斯蒂安·施图普 133 ，穆罕默德·贝尔卡尼 134 ，雅各布·普拉特尼克 135 ，沃洛迪米尔·内维尔科维茨 136 ，卢克·巴斯勒 137 ，马尔科·皮卡多 138 ，费伦茨·让普隆 139 ，尼夫·科恩 94 ，约瑟夫·特卡德莱茨 140 ，保罗·罗苏 141 ，彼得·帕德莱夫斯基 3 ，斯坦尼斯瓦夫·巴尔佐夫斯基 3 ，凯尔·蒙哥马利 69 ，阿琳·梅内塞斯 3 ，阿尔基尔·帕特尔 5,142 ，王子轩 29 ，杰米·塔克-福尔茨 101 ，杰克·斯特德 143 ，汤姆·戈岑 144 ，费雷什特·卡泽米 3 ，杰里迈亚·米尔鲍尔 30 ，约翰·阿诺德·安巴伊 145 ，阿布舍克·舒克拉 146 ，扬·卡洛斯·莱瓦·拉布拉多 26 ，艾伦·吉夫雷 147 ，休·沃尔夫 3 ，维维安·罗斯巴赫 26 ，穆罕默德·法耶兹·阿齐兹 100 ，尤内斯·卡达尔 51 ，陈彦旭 148 ，罗宾·张 32 ，潘佳怡 45 ，安东尼奥·特平 17 ，尼克拉斯·明尼霍夫 7 ，海莉·舍尔科普夫 3 ，埃里克·郑 30 ，阿维希·卡米 149 ，亚当·琼斯 3 ，贾纳姆·沙阿 150 ，伊桑·D·L· 布朗 151 、朱科林 97 、马克斯·巴托洛 152 、理查德·惠勒 107 、安德鲁·何 153 、肖尔·巴坎 154 、王佳琪 8 、马丁·斯特伯格 3 、叶戈尔·克列托夫 155 、考斯塔布·斯里达尔 156 、齐娜布·埃尔-瓦西夫 157 、张安吉 32 、丹尼尔·皮达 158 、乔安娜·谭 159 、大卫·M·坎宁安 160 、弗拉基米尔·戈里亚切夫 3 、德摩斯梯尼·帕特拉马尼斯 51 、迈克尔·克劳斯 161 、安德鲁·雷登蒂 46 、丹尼尔·布加斯 3 、大卫·阿尔杜斯 45 、赖杰欣 162 、香农·科尔曼 49 、莫森·巴哈卢 163 、徐江南 164 、李相元 3 、赵珊迪 26 、唐宁 45 、迈克尔·K·科恩 45 、迈卡·卡罗尔 45 、奥尔·帕拉迪斯 45 、扬·亨德里克·基希纳 165 、斯特凡·施泰纳贝格尔 8 、马克西姆·奥夫钦尼科夫 166 、杰森·O· 马托斯 159 、阿迪蒂亚·谢诺伊 3 、小贝内迪托·阿尔维斯·德奥利维拉 60 、迈克尔·王 45 、聂宇舟 167 、保罗·乔尔达诺 168 、菲利普·彼得森 168 、安娜·什蒂贝尔-贝特利 169 、普里蒂·舒克拉 170 、乔纳森·克罗泽 171 、安东内拉·平托 172 、什雷亚斯·维尔马 173 、普拉尚特·乔希 174 、郑鑫勇 175 、艾莉森·蒂 7 、热雷米·安德烈奥莱蒂 63 、奥赖恩·韦勒 176 、拉加夫·辛格尔 116 、张刚 3 、亚历山大·伊万诺夫 177 、塞里·库里 132 、哈米德·莫斯塔吉米 83 、昆瓦尔·塔曼 178 、陈启佳 101 、陈国庆 179 、雅各布·洛德 15 、斯特凡诺·卡瓦列里 180 、汉娜·斯利克 69 、扎卡里·布朗 32 、乔纳森·罗伯茨 15 、威廉·阿利 3 、孙坤阳 45 、瑞安·斯滕德尔 181 、马克斯·兰帕斯 7 、安卡·鲁埃尔 7 、王婷 69 、徐翰萌 106 、斯里尼瓦斯·古德·拉帕尔蒂 182 、巴勃罗·埃尔南德斯-卡马拉 183 、弗雷迪·马丁 3 、德米特里·马利舍夫 3 、托马斯·普罗伊 184 、托梅克·科尔巴克 185 、马库斯·阿布拉莫维奇 3 、多米尼克·威廉姆森 144 、陈子烨 186 、比罗·巴林特 3 、M·赛富尔·巴里 187 、佩曼·卡萨尼 188 、王梓豪 77 、贝赫扎德·安萨里内贾德 3 、拉克什曼·普拉萨德·戈斯瓦米 146 、 孙烨文 189 ，霍萨姆·埃尔格奈尼 190 ，丹尼尔·托尔代拉 191 ，乔治·巴拉巴尼安 156 ，厄斯·安德森 192 ，琳娜·克维斯塔德 193 ，亚历杭德罗·何塞·莫亚诺 194 ，拉贾特·马赫什瓦里 195 ，艾哈迈德·萨科尔 81 ，穆拉特·埃龙 196 ，艾萨克·C·麦卡利斯特 3 ，哈维尔·希门尼斯 26 ，因诺森特·埃涅奎 3 ，安德鲁·法夫尔 D.O. 197 ，沙伊莱什·沙阿 198 ，周晓翔 53 ，菲鲁兹·卡马洛夫 199 ，罗纳德·克拉克 51 ，舍温·阿卜杜利 172 ，蒂姆·桑滕斯 15 ，哈利达·米尔 26 ，王哈里森·K 101 ，卡利安·拉马克里希南 51 ，埃文·陈 32 ，亚历山德罗·托马西耶洛 200 ，G. 布鲁诺·德·卢卡 7 ，施卓·卢伊 38 ，文卡·勒 45 ，诺姆·科尔特 154 ，尼尔斯·明德勒 17 ，阿维·塞姆勒 51 ，艾玛·罗德曼 201 ，雅各布·德罗里 3 ，卡尔·J·福萨姆 202 ，米林德·贾戈塔 45 ，罗纳克·普拉迪普 117 ，范宏路 203 ，特杰·沙阿 204 ，乔纳森·艾歇尔 205 ，迈克尔·陈 38 ，库沙尔·塔曼 7 ，威廉·梅里尔 94 ，卡特·哈里斯 206 ，杰森·格罗斯 3 ，伊利亚·古谢夫 3 ，阿桑卡亚·夏尔马 207 ，沙尚克·阿格尼霍特里 208 ，帕维尔·热尔诺夫 72 ，西拉努特·乌萨瓦苏察孔 209 ，穆罕默德礼萨·莫法耶齐 72 ，谢尔盖·博格丹诺夫 210 ，亚历山大·皮佩尔斯基 211 ，马克·卡拉乌莱亚努 212 ，张大卫 7 ，迪伦·勒 3 ，罗曼·莱文托夫 213 ，伊格纳特·索罗科 74 ，托尔本·扬森 214 ，帕斯卡尔·劳尔 215,216 ，约书亚·杜尔施 217 ，瓦格·塔马兹扬 218 ，维克托·莫拉克 3 ，马文杰 45 ，威廉·赫尔德 7,135 ，陈德辉 219 ，冼瑞成 100 ，阿梅尔·兰迪·泽巴泽 220 ，穆罕纳德·穆罕默德 221 ，朱利安·诺亚·莱瑟 104 ，米歇尔·X·袁 3 ，莱拉·亚卡尔 222 ，约翰内斯·伦格勒 17 ，侯赛因·沙赫塔什 223 ，埃德森·奥利维拉 224 ，约瑟夫·W· 杰克逊 225 ，丹尼尔·埃斯皮诺萨·冈萨雷斯 167 ，安迪·邹 30,226 ，穆图·奇丹巴拉姆 141 ，蒂莫西·马尼克 3 ，赫克托·哈芬登 3 ，达希尔·斯坦德 227 ，阿里·达苏奇 176 ，亚历山大·沈 228 ，埃米利安·杜克 17 ，比塔·戈尔沙尼 3 ，大卫·斯塔普 148 ，米卡莱·乌祖 229 ，阿丽娜·鲍里索夫娜·日德科夫斯卡娅 230 ，卢卡斯·勒瓦克 17 ，马蒂亚斯·文采 231,232 ，达斯汀·韦尔 3 ，科林·唐 30 ，扎基·侯赛因 233 ，肖恩·菲利普斯 3 ，姜慕真 3 ，弗雷德里克·埃克斯特伦 3 ，安吉拉·哈蒙 3 ，奥姆·帕特尔 101 ，尼古拉斯·雷米 234 ，法拉兹·法尔希迪 235 ，乔治·梅德利 3 ，福鲁格·穆罕默德扎德 3 ，马德琳·佩尼亚弗洛尔 236 ，海勒·卡萨洪 5 ，阿莱娜·弗里德里希 237 ，克莱尔·斯帕罗 77 ，陶姆·萨卡尔 167 ，奥姆卡尔·达马内 238 ，阿里·哈杰吉利·米拉巴迪 49 ，埃里克·霍尔曼 3 ，迈克·巴塔利亚 3 ，穆罕默德·马格苏迪梅赫拉巴尼 239 ，孝煌 240 ，阿隆·阿米特 241 ，戴夫·赫尔伯特 3 ，罗伯托·佩雷拉 242 ，西蒙·韦伯 17 ，斯蒂芬·门萨 243 ，内森·安德烈 244 ，安东·佩里斯蒂 3 ，克里斯·哈贾迪 7 ，希曼舒·古普塔 99 ，斯蒂芬·马利纳 245 ，塞缪尔·阿尔巴尼 3 ，威尔·蔡 45 ，穆斯塔法·梅哈卡里 72,246 ，弗兰克·赖德格尔德 3 ， 安娜-卡塔琳娜·迪克 59 ，卡里·弗莱迪 247 ，贾斯迪普·西杜 3 ，金完永 248 ，玛丽安娜·科斯塔 26 ，胡贝布·古尔杜安 79 ，布莱恩·韦伯 249 ，哈什·库马尔 250 ，姜彤 101 ，阿鲁尼姆·阿加瓦尔 251 ，基亚拉·切科内洛 3 ，沃伦·S·瓦斯 3 ，庄超 3 ，朴浩恩 252,253 ，安德鲁·R·塔菲克 8 ，达塔维亚·阿加瓦尔 15 ，迈克尔·基希霍夫 59 ，戴林杰 32 ，埃文·金 32 ，约翰·费雷特 73 ，王宇舟 135 ，严明昊 85 ，克日什托夫·布尔齐 8 ，张立新 26 ，安东尼奥·弗兰卡 15 ，戴安娜·T·范 254 ，罗康勇 7 ，约书亚·罗宾逊 255 ，什林·古尔 256 ，古扬·查布拉尼 135 ，杜哲航 156 ，阿德里安·科斯马 257 ，科林·怀特 258 ，罗宾·里布莱特 108 ，普拉吉维·萨克塞纳 259 ，雅各布·沃塔瓦 29 ，弗拉基米尔·温尼科夫 3 ，伊桑·德莱尼 260 ，希夫·哈拉西亚马尼 261 ，赛义德·M· 沙希德 262 、让-克里斯托夫·穆拉 70,263 、拉夫尔·韦托什金 264 、雷纳斯·巴乔 265 、文森特·吉尼斯 92,101 、亚历山大·马克萨佩强 26 、弗洛伦西亚·德拉罗莎 266 、李修宇 45 、纪尧姆·马洛 267 、莱昂·朗 148 、朱利安·洛朗多 50 、法蒂玛·阿德桑亚 26,268 、朱利安·波蒂埃 15 、劳伦斯·霍洛姆 15 、维克托·索萨 15 、周安娜 269 、伊吉特·亚林 270 、格本加·丹尼尔·奥比科亚 3 、卢卡·阿尔纳博尔迪 50 、雷（迈克尔·波科尔尼） 271 、菲利波·比吉 50 、卡纽尔·巴乔 107 、皮埃尔·克拉维耶 272 、加布里埃尔·雷基亚 273 、玛拉·波佩斯库 274 、尼基塔·舒尔加 275 、恩格福·米尔德里德·坦维 276 、托马斯·C.H. 卢克斯 277 , 本·兰克 3 , 柯林·倪 79 , 阿列西亚·雅基姆奇克 278 , 刘焕旭（奎因） 279 , 奥勒·海格斯特伦 280 , 埃米尔·维尔卡马 281 , 希曼舒·纳拉扬 3 , 汉斯·冈德拉赫 32 , 莱奥诺尔·布里托-桑塔纳 282 , 布莱恩·阿马罗 7 , 维韦克·瓦吉佩 7 , 瑞娜·格罗弗 135 , 范一阳 3 , 加布里埃尔·波埃西亚·雷斯·席尔瓦 7 , 辛林伟 77 , 约西·克拉蒂什 136 , 雅各布·武茨基 17 , 李文鼎 127 , 贾斯汀·徐 51 , 凯文·约瑟夫·斯卡里亚 99 , 弗雷迪·瓦格斯 283 , 法尔扎德·哈比比 284 , 龙（托尼）连 45 , 埃马努埃莱·罗多拉 56 , 朱尔斯·罗宾斯 3 , 文森特·郑 9 , 德克兰·格拉布 7 , 艾达·博西奥 285 , 托尼·弗吕霍夫 3 , 伊多·阿科夫 286 , 伊芙·J·Y·罗 287 , 齐浩 186 , 蒋曦 77 , 本·塞格夫 46 , 范景轩 101 , 莎拉·马丁森 101 , 王奕元 101 , 凯莉·豪斯内希特 101 , 迈克尔·P· 布伦纳 101 、毛毛 186 、江一博 77 、张欣宇 186 、大卫·阿瓦吉安 208 、埃肖恩·杰西卡·西皮奥 288 、穆罕默德·雷汉·西迪基 289,290 、阿隆·拉戈勒 291 、贾斯汀·谭 15 、迪帕库马尔·帕蒂尔 292 、雷贝卡·普莱奇尼克 3 、亚伦·柯特兰 175 、罗斯林·格雷斯·蒙特西略 293 、斯特凡·杜兰德 294 、奥马尔·法鲁克·博杜尔 3 、扎赫拉·阿杜尔 295 、穆罕默德·泽克里 296 、纪尧姆·杜维尔 26 、阿里·卡拉科奇 297 、塔尼亚·C·B· 桑托斯 3 、萨米尔·沙姆塞尔丁 298 、卢克曼·卡里姆 246 、安娜·利亚霍维茨卡娅 299 、内特·雷斯曼 300 、尼古拉斯·法里纳 26 、胡安·卡洛斯·冈萨雷斯 301 、加布·马扬 186 、莎拉·霍巴克 101 、罗德里戈·德奥利维拉·佩纳 302 、格伦·谢尔曼 26 、霍贾特·马里吉 3 、拉苏尔·普里亚马内什 3 、吴文涛 49 、格兹德努尔·德米尔 3 、桑德拉·门多萨 303,304 、伊斯梅尔·阿拉拉布 305 、约书亚·科尔 306 、丹耶尔·费雷拉 26 、布莱恩·约翰逊 307 、萧云·米利伦 308 、穆罕默德·萨夫达里 309 、戴良体 51 、西里潘·阿通图拉苏克 26 、阿列克谢·普罗宁 310 、范静 274 、安赫尔·拉米雷斯-特里尼达德 3 、阿什利·卡特赖特 311 、达菲尼·波特迈尔 312 、奥米德·塔赫里 313 、大卫·乌捷夫斯基 314 、斯坦利·斯特帕尼克 315 、塞缪尔·佩里 3 、卢克·阿斯丘 316 、劳尔·阿德里安·韦尔塔·罗德里格斯 3 、阿卜杜勒卡德尔·丹丹 26 、萨姆·阿里 58 、里卡多·洛雷纳 317 、克里希纳穆尔蒂·艾耶 318 、斯凯·穆罕默德·萨劳丁 319 、穆拉特·伊斯兰 320 、胡安·冈萨雷斯 3 、乔什·杜西 321 、拉塞尔·坎贝尔 322 、玛雅·索姆拉克 3 、瓦西里奥斯·马夫鲁迪斯 323 、埃里克·维尔戈 3 、秦珏航 324 、本亚明·博尔巴什 325 、埃里克·朱 73 、杰克·林赛 165 、阿尼尔·拉达克里希南 171 、 安托万·雅隆 3 ，I.M.J. 麦金尼斯 3 ，亚历克斯·胡佛 77 ，索伦·默勒 326 ，宋边 85 ，约翰·赖 26 ，特贾尔·帕特瓦丹 271

Affiliations  所属机构

1. 3. 
    
    Independent Researcher  独立研究员
    
2. 4. 
    
    Texas A&M University  德克萨斯农工大学
    
3. 5. 
    
    McGill University  麦吉尔大学
    
4. 6. 
    
    Queen’s University  女王大学
    
5. 7. 
    
    Stanford University  斯坦福大学
    
6. 8. 
    
    University of Washington  
    华盛顿大学
    
7. 9. 
    
    University of California, San Diego  
    加州大学圣地亚哥分校
    
8. 10. 
    
    RWTH Aachen University  亚琛工业大学
    
9. 11. 
    
    Pondicherry Engineering College  
    本地治里工程学院
    
10. 12. 
    
    Institute of Mathematics of NAS of Ukraine  
    乌克兰国家科学院数学研究所
    
11. 13. 
    
    ELTE  罗兰大学
    
12. 14. 
    
    University of Porto  波尔图大学
    
13. 15. 
    
    University of Cambridge  剑桥大学
    
14. 16. 
    
    Kyiv Polytechnic Institute  
    基辅理工学院
    
15. 17. 
    
    ETH Zürich  苏黎世联邦理工学院
    
16. 18. 
    
    Nimbus AI
    
17. 19. 
    
    Georgia Southern University  
    佐治亚南方大学
    
18. 20. 
    
    Durham University  杜伦大学
    
19. 21. 
    
    University of Minnesota Twin Cities  
    明尼苏达大学双城分校
    
20. 22. 
    
    Queen Mary University of London  
    伦敦玛丽女王大学
    
21. 23. 
    
    Alberta Health Services  阿尔伯塔省卫生服务局
    
22. 24. 
    
    Microsoft Research  微软研究院
    
23. 25. 
    
    ZG Law  ZG 律师事务所
    
24. 26. 
    
    Outlier
    
25. 27. 
    
    Hereford College of Arts  
    赫里福德艺术学院
    
26. 28. 
    
    Auckland University of Technology  
    奥克兰理工大学
    
27. 29. 
    
    Princeton University  普林斯顿大学
    
28. 30. 
    
    Carnegie Mellon University  
    卡内基梅隆大学
    
29. 31. 
    
    Hemwati Nandan Bahuguna Garhwal University  
    赫姆瓦蒂·南丹·巴胡古纳加尔瓦尔大学
    
30. 32. 
    
    Massachusetts Institute of Technology  
    麻省理工学院
    
31. 33. 
    
    Accenture Labs  埃森哲实验室
    
32. 34. 
    
    Escuela Superior de Medicina- Instituto Politécnico Nacional  
    国立理工学院高等医学院
    
33. 35. 
    
    CICMA
    
34. 36. 
    
    University of Canterbury  
    坎特伯雷大学
    
35. 37. 
    
    Metropolitan State University of Denver  
    丹佛大都会州立大学
    
36. 38. 
    
    California Institute of Technology  
    加州理工学院
    
37. 39. 
    
    Université de Yaoundé I  
    雅温得第一大学
    
38. 40. 
    
    Ecole Nationale Supérieure Polytechnique de Yaoundé  
    雅温得国立高等综合理工学院
    
39. 41. 
    
    Tanta University  坦塔大学
    
40. 42. 
    
    Tufts University  塔夫茨大学
    
41. 43. 
    
    The Jackson Laboratory  杰克逊实验室
    
42. 44. 
    
    Inria  法国国家信息与自动化研究所
    
43. 45. 
    
    University of California, Berkeley  
    加州大学伯克利分校
    
44. 46. 
    
    Columbia University  哥伦比亚大学
    
45. 47. 
    
    Institute of Science and Technology Austria  
    奥地利科学技术学院
    
46. 48. 
    
    RUSM  罗斯大学
    
47. 49. 
    
    University of British Columbia  
    不列颠哥伦比亚大学
    
48. 50. 
    
    École Polytechnique Fédérale de Lausanne  
    洛桑联邦理工学院
    
49. 51. 
    
    University of Oxford  牛津大学
    
50. 52. 
    
    Charité – Universitätsmedizin  
    夏里特大学医院
    
51. 53. 
    
    Humboldt-Universität zu Berlin  
    柏林洪堡大学
    
52. 54. 
    
    Happy Technologies LLC  快乐科技有限公司
    
53. 55. 
    
    Northern Illinois University  
    北伊利诺伊大学
    
54. 56. 
    
    Sapienza University of Rome  
    罗马大学
    
55. 57. 
    
    National University of Singapore  
    新加坡国立大学
    
56. 58. 
    
    University of Southern California  
    南加州大学
    
57. 59. 
    
    University of Tübingen  蒂宾根大学
    
58. 60. 
    
    University of Sao Paulo  
    圣保罗大学
    
59. 61. 
    
    Universidade Federal de Juiz de Fora  
    茹伊斯迪福拉联邦大学
    
60. 62. 
    
    Sorbonne Université  索邦大学
    
61. 63. 
    
    École Normale Supérieure  
    巴黎高等师范学院
    
62. 64. 
    
    C. N. Yang institute for Theoretical Physics  
    杨振宁理论物理研究所
    
63. 65. 
    
    University of Luxembourg  
    卢森堡大学
    
64. 66. 
    
    University of Malaya  马来亚大学
    
65. 67. 
    
    Rockwell Automation  罗克韦尔自动化
    
66. 68. 
    
    Contramont Research  康特拉蒙特研究
    
67. 69. 
    
    Washington University  华盛顿大学
    
68. 70. 
    
    CNRS  法国国家科学研究中心
    
69. 71. 
    
    Université Paris-Saclay  巴黎-萨克雷大学
    
70. 72. 
    
    University of Toronto  多伦多大学
    
71. 73. 
    
    Google DeepMind  谷歌深度思维
    
72. 74. 
    
    University of North Texas  
    北德克萨斯大学
    
73. 75. 
    
    Institut Polytechnique de Paris  
    巴黎综合理工学院
    
74. 76. 
    
    TRR Designs  TRR 设计公司
    
75. 77. 
    
    University of Chicago  芝加哥大学
    
76. 78. 
    
    Maastricht University  马斯特里赫特大学
    
77. 79. 
    
    University of California, Los Angeles  
    加州大学洛杉矶分校
    
78. 80. 
    
    Martin-Luther-University Halle-Wittenberg  
    马丁·路德大学哈勒-维滕贝格
    
79. 81. 
    
    Leibniz University Hannover  
    汉诺威莱布尼茨大学
    
80. 82. 
    
    Indian Institute of Technology Bombay  
    孟买印度理工学院
    
81. 83. 
    
    University of Calgary  卡尔加里大学
    
82. 84. 
    
    Institute for Molecular Manufacturing  
    分子制造研究所
    
83. 85. 
    
    University of Wisconsin-Madison  
    威斯康星大学麦迪逊分校
    
84. 86. 
    
    University of Michigan  密歇根大学
    
85. 87. 
    
    Bethune-Cookman University  
    贝瑟尼-库克曼大学
    
86. 88. 
    
    St. Petersburg College  圣彼得堡学院
    
87. 89. 
    
    La Molina National Agrarian University  
    拉莫利纳国立农业大学
    
88. 90. 
    
    University of Bath  巴斯大学
    
89. 91. 
    
    National University Philippines  
    菲律宾国立大学
    
90. 92. 
    
    Vrije Universiteit Brussel  
    布鲁塞尔自由大学
    
91. 93. 
    
    PeopleTec, Inc.  PeopleTec 公司
    
92. 94. 
    
    New York University  纽约大学
    
93. 95. 
    
    Technion – Israel Institute of Technology  
    以色列理工学院
    
94. 96. 
    
    University of Miami  迈阿密大学
    
95. 97. 
    
    University of Maryland  马里兰大学
    
96. 98. 
    
    Technische Universität Berlin  
    柏林工业大学
    
97. 99. 
    
    Arizona State University  
    亚利桑那州立大学
    
98. 100. 
    
    University of Illinois Urbana-Champaign  
    伊利诺伊大学厄巴纳-香槟分校
    
99. 101. 
    
    Harvard University  哈佛大学
    
100. 102. 
    
    Royal Holloway, University of London  
    伦敦大学皇家霍洛威学院
    
101. 103. 
    
    Universidad Iberoamericana  
    伊比利亚美洲大学
    
102. 104. 
    
    TU Wien  维也纳工业大学
    
103. 105. 
    
    Swinburne University of Technology  
    斯威本科技大学
    
104. 106. 
    
    Yale University  耶鲁大学
    
105. 107. 
    
    University of Edinburgh  爱丁堡大学
    
106. 108. 
    
    École Normale Supérieure Paris-Saclay  
    巴黎萨克雷高等师范学校
    
107. 109. 
    
    National Information Processing Institute  
    国家信息处理研究所
    
108. 110. 
    
    University College London  
    伦敦大学学院
    
109. 111. 
    
    Ecco IT  埃科信息技术
    
110. 112. 
    
    University of Western Australia  
    西澳大利亚大学
    
111. 113. 
    
    Snorkel AI  斯诺克尔人工智能公司
    
112. 114. 
    
    Indiana State University  
    印第安纳州立大学
    
113. 115. 
    
    Oxford University  牛津大学
    
114. 116. 
    
    Mohamed bin Zayed University of Artificial Intelligence  
    穆罕默德·本·扎耶德人工智能大学
    
115. 117. 
    
    University of Waterloo  滑铁卢大学
    
116. 118. 
    
    Manhattan School of Music  
    曼哈顿音乐学院
    
117. 119. 
    
    Universiteit Leiden  莱顿大学
    
118. 120. 
    
    Synbionix  辛比奥尼克斯
    
119. 121. 
    
    Corteva Agriscience  科迪华农业科技
    
120. 122. 
    
    Diverging Mathematics  发散数学
    
121. 123. 
    
    Saint Mary’s University  圣玛丽大学
    
122. 124. 
    
    Emory University  埃默里大学
    
123. 125. 
    
    Sanford Burnham Preybs  桑福德·伯纳姆·普雷比斯医学研究所
    
124. 126. 
    
    Yonsei University  延世大学
    
125. 127. 
    
    Cornell University  康奈尔大学
    
126. 128. 
    
    University of Leeds  利兹大学
    
127. 129. 
    
    Politecnico di Milano  米兰理工大学
    
128. 130. 
    
    KU Leuven  鲁汶大学
    
129. 131. 
    
    Brandenburg University of Technology  
    勃兰登堡工业大学
    
130. 132. 
    
    INSAIT  索非亚信息、通信与知识技术研究所
    
131. 133. 
    
    Ruhr University Bochum  波鸿鲁尔大学
    
132. 134. 
    
    University Mohammed I  穆罕默德一世大学
    
133. 135. 
    
    Georgia Institute of Technology  
    佐治亚理工学院
    
134. 136. 
    
    Northwestern University  西北大学
    
135. 137. 
    
    University of Arizona  亚利桑那大学
    
136. 138. 
    
    Universidade de Lisboa,  里斯本大学
    
137. 139. 
    
    Mānuka Honey and Beekeeping Consultancy Ltd  
    麦卢卡蜂蜜与养蜂咨询有限公司
    
138. 140. 
    
    Charles University  查理大学
    
139. 141. 
    
    Duke University  杜克大学
    
140. 142. 
    
    Mila  米拉
    
141. 143. 
    
    University of Copenhagen  
    哥本哈根大学
    
142. 144. 
    
    The University of Sydney  
    悉尼大学
    
143. 145. 
    
    University of Technology Sydney  
    悉尼科技大学
    
144. 146. 
    
    Indian Institute of Technology Delhi  
    印度理工学院德里分校
    
145. 147. 
    
    University of Buenos Aires  
    布宜诺斯艾利斯大学
    
146. 148. 
    
    University of Amsterdam  阿姆斯特丹大学
    
147. 149. 
    
    Ben-Gurion University  本-古里安大学
    
148. 150. 
    
    blurrylogic  模糊逻辑
    
149. 151. 
    
    Donald and Barbara Zucker School of Medicine  
    唐纳德与芭芭拉·朱克医学院
    
150. 152. 
    
    Cohere
    
151. 153. 
    
    Ivy Natal
    
152. 154. 
    
    Hebrew University  希伯来大学
    
153. 155. 
    
    Fraunhofer IMTE  弗劳恩霍夫 IMTE
    
154. 156. 
    
    University of Pennsylvania  
    宾夕法尼亚大学
    
155. 157. 
    
    National Institute of Laser Enhanced Sciences  
    国家激光增强科学研究所
    
156. 158. 
    
    Drexel University  德雷塞尔大学
    
157. 159. 
    
    Northeastern University  东北大学
    
158. 160. 
    
    EHC Investments LLC  EHC 投资有限责任公司
    
159. 161. 
    
    University of Windsor  温莎大学
    
160. 162. 
    
    St. Jude Children’s Research Hospital  
    圣裘德儿童研究医院
    
161. 163. 
    
    GC
    
162. 164. 
    
    Rochester Institute of Technology  
    罗切斯特理工学院
    
163. 165. 
    
    Anthropic
    
164. 166. 
    
    CERN  欧洲核子研究中心
    
165. 167. 
    
    University of California, Santa Barbara  
    加州大学圣塔芭芭拉分校
    
166. 168. 
    
    University of Vienna  维也纳大学
    
167. 169. 
    
    Warsaw University of Technology  
    华沙理工大学
    
168. 170. 
    
    EF Polymers Pvt Ltd  
    EF 聚合物私人有限公司
    
169. 171. 
    
    North Carolina State University  
    北卡罗来纳州立大学
    
170. 172. 
    
    Independent researcher  独立研究员
    
171. 173. 
    
    Simplr AI, Asurion
    
172. 174. 
    
    All India Institute of Medical Sciences  
    全印度医学科学研究所
    
173. 175. 
    
    Brown University  布朗大学
    
174. 176. 
    
    Johns Hopkins University  
    约翰斯·霍普金斯大学
    
175. 177. 
    
    Ruhr-Universität Bochum  波鸿鲁尔大学
    
176. 178. 
    
    Standard Intelligence  标准智能
    
177. 179. 
    
    Posts and Telecommunications Institute of Technology  
    邮电技术学院
    
178. 180. 
    
    Clearhorse Ltd  清马有限公司
    
179. 181. 
    
    Cranfield University  克兰菲尔德大学
    
180. 182. 
    
    JNTU  贾瓦哈拉尔·尼赫鲁科技大学
    
181. 183. 
    
    Image Processing Lab, Universitat de Valencia  
    瓦伦西亚大学图像处理实验室
    
182. 184. 
    
    Universität Zürich  苏黎世大学
    
183. 185. 
    
    UK AI Safety Institute  
    英国人工智能安全研究所
    
184. 186. 
    
    Boston University  波士顿大学
    
185. 187. 
    
    SDAIA  沙特阿拉伯数据和人工智能局
    
186. 188. 
    
    Children’s Hospital of Orange County  
    奥兰治县儿童医院
    
187. 189. 
    
    The Ohio State University  
    俄亥俄州立大学
    
188. 190. 
    
    Cairo University Specialized Pediatric Hospital  
    开罗大学专科儿科医院
    
189. 191. 
    
    Universidad de Valencia  瓦伦西亚大学
    
190. 192. 
    
    University of Arkansas  阿肯色大学
    
191. 193. 
    
    Monash University  莫纳什大学
    
192. 194. 
    
    OncoPrecision
    
193. 195. 
    
    Genomia Diagnostics Research Pvt Ltd
    
194. 196. 
    
    IEEE Life Member  IEEE 终身会员
    
195. 197. 
    
    Larkin Community Hospital  
    拉金社区医院
    
196. 198. 
    
    The University of Texas at Dallas  
    德克萨斯大学达拉斯分校
    
197. 199. 
    
    Canadian University Dubai  
    迪拜加拿大大学
    
198. 200. 
    
    Università di Milano-Bicocca  
    米兰比可卡大学
    
199. 201. 
    
    University of Massachusetts Lowell  
    马萨诸塞大学洛厄尔分校
    
200. 202. 
    
    Virginia Tech  弗吉尼亚理工大学
    
201. 203. 
    
    University of Geneva  日内瓦大学
    
202. 204. 
    
    Rutgers University  罗格斯大学
    
203. 205. 
    
    MolMind
    
204. 206. 
    
    Cal Poly San Luis Obispo  
    加州州立理工大学圣路易斯奥比斯波分校
    
205. 207. 
    
    Patched Codes, Inc
    
206. 208. 
    
    University of Mannheim  曼海姆大学
    
207. 209. 
    
    Chulalongkorn University  
    朱拉隆功大学
    
208. 210. 
    
    Ecole polytechnique  巴黎综合理工学院
    
209. 211. 
    
    Stockholm University  斯德哥尔摩大学
    
210. 212. 
    
    AE Studio  AE 工作室
    
211. 213. 
    
    Gaia Lab  盖亚实验室
    
212. 214. 
    
    Leibniz Institute for Science and Mathematics Education  
    莱布尼茨科学与数学教育研究所
    
213. 215. 
    
    Australian National University  
    澳大利亚国立大学
    
214. 216. 
    
    Saarland University  萨尔大学
    
215. 217. 
    
    College of Eastern Idaho  
    东爱达荷学院
    
216. 218. 
    
    Intrinsic Innovation LLC
    
217. 219. 
    
    HUTECH
    
218. 220. 
    
    INRIA
    
219. 221. 
    
    King Saud University  沙特国王大学
    
220. 222. 
    
    Universidad de Buenos Aires  
    布宜诺斯艾利斯大学
    
221. 223. 
    
    Pennsylvania College of Technology  
    宾夕法尼亚理工学院
    
222. 224. 
    
    CERo Therapeutics Holdings, Inc.  
    CERo 治疗控股公司
    
223. 225. 
    
    The Univeirsty of Tennessee  
    田纳西大学
    
224. 226. 
    
    Gray Swan AI  灰天鹅 AI
    
225. 227. 
    
    EleutherAI
    
226. 228. 
    
    University of Montpellier  
    蒙彼利埃大学
    
227. 229. 
    
    HomeEquity Bank  HomeEquity 银行
    
228. 230. 
    
    Materials Platform for Data Science LLC  
    材料数据科学平台有限责任公司
    
229. 231. 
    
    University of Trento  特伦托大学
    
230. 232. 
    
    Fondazione Bruno Kessler  
    布鲁诺·凯斯勒基金会
    
231. 233. 
    
    Cambridge University  剑桥大学
    
232. 234. 
    
    LGM
    
233. 235. 
    
    Georgia State University  
    佐治亚州立大学
    
234. 236. 
    
    Polytechnic University of the Philippines  
    菲律宾理工大学
    
235. 237. 
    
    University of Oregon  俄勒冈大学
    
236. 238. 
    
    University of Mumbai  孟买大学
    
237. 239. 
    
    University of Guelph  圭尔夫大学
    
238. 240. 
    
    Case Wester Reserve University  
    凯斯西储大学
    
239. 241. 
    
    Intuit  直觉公司
    
240. 242. 
    
    CTTC / CERCA
    
241. 243. 
    
    National University  国立大学
    
242. 244. 
    
    Talishar  塔利沙尔
    
243. 245. 
    
    Dyno Therapeutics  迪诺治疗公司
    
244. 246. 
    
    The Hospital for Sick Children  
    病童医院
    
245. 247. 
    
    Lewis Katz School of Medicine  
    刘易斯·卡茨医学院
    
246. 248. 
    
    Fyaora Labs  菲亚奥拉实验室
    
247. 249. 
    
    Intelligent Geometries  智能几何学
    
248. 250. 
    
    Indian Institute of Technology (BHU)  
    印度理工学院（瓦拉纳西校区）
    
249. 251. 
    
    Center for AI Safety  
    人工智能安全中心
    
250. 252. 
    
    AIM Intelligence  AIM 智能
    
251. 253. 
    
    Seoul National University  
    首尔国立大学
    
252. 254. 
    
    The University of Texas at Arlington  
    德克萨斯大学阿灵顿分校
    
253. 255. 
    
    The Hartree Centre  哈特里中心
    
254. 256. 
    
    Missouri University of Science and Technology  
    密苏里科技大学
    
255. 257. 
    
    POLITEHNICA Bucharest National University of Science and Technology  
    布加勒斯特理工大学
    
256. 258. 
    
    Abacus.AI
    
257. 259. 
    
    German Research Center for Artificial Intelligence  
    德国人工智能研究中心
    
258. 260. 
    
    University of Galway  爱尔兰国立大学高威分校
    
259. 261. 
    
    University of Houston  休斯顿大学
    
260. 262. 
    
    Eastern Institute of Technology (EIT)  
    东部理工学院
    
261. 263. 
    
    ENS Lyon  里昂高等师范学院
    
262. 264. 
    
    Czech Technical University in Prague  
    布拉格捷克理工大学
    
263. 265. 
    
    CISPA Helmholtz Center for Information Security  
    CISPA 亥姆霍兹信息安全中心
    
264. 266. 
    
    Universidad de Morón  莫龙大学
    
265. 267. 
    
    Université Paris Cité and Sorbonne Université  
    巴黎西岱大学与索邦大学
    
266. 268. 
    
    Sheffield Hallam University  
    谢菲尔德哈勒姆大学
    
267. 269. 
    
    The New School  新学院
    
268. 270. 
    
    Max Planck Institute for Software Systems  
    马克斯·普朗克软件系统研究所
    
269. 271. 
    
    OpenAI
    
270. 272. 
    
    École Polytechnique  巴黎综合理工学院
    
271. 273. 
    
    Modulo Research  模运算研究
    
272. 274. 
    
    Heidelberg University  海德堡大学
    
273. 275. 
    
    La Trobe University  拉筹伯大学
    
274. 276. 
    
    University of Yaoundé I  
    雅温得第一大学
    
275. 277. 
    
    Lux Labs
    
276. 278. 
    
    University of Innsbruck  因斯布鲁克大学
    
277. 279. 
    
    Nabu Technologies Inc
    
278. 280. 
    
    Chalmers University of Technology  
    查尔姆斯理工大学
    
279. 281. 
    
    KTH Royal Institute of Technology  
    瑞典皇家理工学院
    
280. 282. 
    
    Unidade Local de Saúde de Lisboa Ocidental  
    里斯本西部地方卫生局
    
281. 283. 
    
    Quotient AI  商数人工智能公司
    
282. 284. 
    
    University of California, Irvine  
    加州大学尔湾分校
    
283. 285. 
    
    University of Padua  帕多瓦大学
    
284. 286. 
    
    Aalto University  阿尔托大学
    
285. 287. 
    
    Royal Veterinary College  
    皇家兽医学院
    
286. 288. 
    
    The Future Paralegals of America  
    美国未来律师协会
    
287. 289. 
    
    RMIT University  皇家墨尔本理工大学
    
288. 290. 
    
    Universal Higher Education  
    普及高等教育
    
289. 291. 
    
    Eastlake High School  东湖高中
    
290. 292. 
    
    CSMSS Chh. Shahu College of Engineering  
    CSMSS Chh. Shahu 工程学院
    
291. 293. 
    
    Central Mindanao University  
    中棉兰老大学
    
292. 294. 
    
    University of Montreal  蒙特利尔大学
    
293. 295. 
    
    University of Bradford  布拉德福德大学
    
294. 296. 
    
    Beni Suef University  贝尼苏韦夫大学
    
295. 297. 
    
    Bogazici University  博阿齐奇大学
    
296. 298. 
    
    Mansoura University  曼苏拉大学
    
297. 299. 
    
    Univerisity of Bristol  布里斯托大学
    
298. 300. 
    
    University of Oklahoma  俄克拉荷马大学
    
299. 301. 
    
    Jala University  哈拉大学
    
300. 302. 
    
    Florida Atlantic University  
    佛罗里达大西洋大学
    
301. 303. 
    
    CONICET  阿根廷国家科学与技术研究委员会
    
302. 304. 
    
    Universidad Tecnológica Nacional  
    国立技术大学
    
303. 305. 
    
    Bournemouth University  伯恩茅斯大学
    
304. 306. 
    
    University of Warwick  华威大学
    
305. 307. 
    
    University of Alabama Huntsville  
    阿拉巴马大学亨茨维尔分校
    
306. 308. 
    
    Van Andel Institute  范安德尔研究所
    
307. 309. 
    
    University of Hertfordshire  
    赫特福德大学
    
308. 310. 
    
    Central College  中央学院
    
309. 311. 
    
    Sheffield Teaching Hospitals NHS Foundation Trust  
    谢菲尔德教学医院国民保健服务基金会信托
    
310. 312. 
    
    Nottingham Trent University  
    诺丁汉特伦特大学
    
311. 313. 
    
    Max Planck Institute for Intelligent Systems  
    马克斯·普朗克智能系统研究所
    
312. 314. 
    
    Outevsky Bespoke Dance Education  
    奥捷夫斯基定制舞蹈教育
    
313. 315. 
    
    University of Virginia  弗吉尼亚大学
    
314. 316. 
    
    Dartmouth College  达特茅斯学院
    
315. 317. 
    
    INESC Microsistemas e Nanotecnologias  
    INESC 微系统与纳米技术研究所
    
316. 318. 
    
    University of Minnesota  明尼苏达大学
    
317. 319. 
    
    Aligarh Muslim University  
    阿里格尔穆斯林大学
    
318. 320. 
    
    John Crane UK Ltd  
    约翰·克兰英国有限公司
    
319. 321. 
    
    James Madison University  
    詹姆斯·麦迪逊大学
    
320. 322. 
    
    University of the Fraser Valley  
    弗雷泽河谷大学
    
321. 323. 
    
    Alan Turing Institute  艾伦·图灵研究所
    
322. 324. 
    
    Rice University  莱斯大学
    
323. 325. 
    
    HUN-REN  匈牙利科学院
    
324. 326. 
    
    Forschungszentrum Jülich  
    于利希研究中心
    

## Appendix BDataset  附录 B 数据集

### B.1Submission Process  B.1 提交流程

To ensure question difficulty, we automatically check the accuracy of frontier LLMs on each question prior to submission. Our testing process uses multi-modal LLMs for text-and-image questions (GPT-4o, Gemini 1.5 Pro, Claude 3.5 Sonnet, o1) and adds two non-multi-modal models (o1-mini, o1-preview) for text-only questions. We use different submission criteria by question type: exact-match questions must stump all models, while multiple-choice questions must stump all but one model to account for potential lucky guesses. Users are instructed to only submit questions that meet this criteria. We note due to non-determinism in models and a non-zero floor in multiple-choice questions, further evaluation on the dataset exhibits some low but non-zero accuracy.  
为确保题目难度，我们在提交前会自动检查前沿 LLMs 对每道题的准确率。我们的测试流程针对图文题使用多模态 LLMs（GPT-4o、Gemini 1.5 Pro、Claude 3.5 Sonnet、o1），针对纯文本题则额外增加两个非多模态模型（o1-mini、o1-preview）。我们根据题型采用不同的提交标准：精确匹配题必须难倒所有模型，而选择题则允许一个模型通过（以考虑可能的侥幸猜对情况）。我们要求用户仅提交符合此标准的题目。需要说明的是，由于模型存在非确定性且选择题存在非零基准准确率，对数据集的进一步评估显示其准确率虽低但并非为零。

We use a standardized system prompt ([Section˜C.1.1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS1.SSS1 "C.1.1 Evaluation ‣ C.1 Prompts ‣ Appendix C Evaluation ‣ Humanity’s Last Exam")) to structure model responses into “Reasoning” and “Final Answer” formatting, and employ an automated GPT-4o judge to evaluate response correctness against the provided answers.  
我们使用标准化系统提示（章节˜C.1.1）将模型响应结构化为“推理过程”和“最终答案”格式，并采用自动化 GPT-4o 评判器根据提供的答案评估响应正确性。

### B.2Human Review Instructions  
B.2 人工审核指南

Questions which merely stump models are not necessarily high quality – they could simply be adversarial to models without testing advanced knowledge. To resolve this, we employ two rounds of human review to ensure our dataset is thorough and sufficiently challenging as determined by human experts in their respective domains.  
仅仅难住模型的问题未必是高质量的——它们可能只是对模型具有对抗性，而没有测试到高级知识。为了解决这个问题，我们采用了两轮人工评审，以确保我们的数据集是全面的，并且按照各自领域的人类专家判断具有足够的挑战性。

#### B.2.1Review Round 1  B.2.1 第一轮评审

We recruit human subject expert reviewers to score, provide feedback, and iteratively refine all user submitted questions. This is similar to the peer review process in academic research, where reviewers give feedback to help question submitters create better questions. We train all reviewers on the instructions and rubric below.  
我们招募人类学科专家评审员对所有用户提交的问题进行评分、提供反馈并迭代改进。这类似于学术研究中的同行评审过程，评审员通过反馈帮助问题提交者创建更好的问题。我们根据以下说明和评分标准对所有评审员进行培训。

##### Reviewer Instructions  评审员说明

- • 
    
    Questions should usually (but do not always need to) be at a graduate / PhD level or above. (Score 0 if the question is not complex enough and AI models can answer it correctly.)  
    问题通常（但并非总是必须）应达到研究生/博士水平或更高。（若问题不够复杂且 AI 模型能正确回答，则得 0 分。）
    
    - – 
        
        If the model is not able to answer correctly and the question is below a graduate level, the question can be acceptable.  
        如果模型无法正确回答且问题低于研究生水平，该问题也可接受。
        
    
- • 
    
    Questions can be any field across STEM, law, history, psychology, philosophy, trivia, etc. as long as they are tough and interesting questions.  
    问题可涵盖 STEM、法律、历史、心理学、哲学、冷知识等任何领域，只要它们是既困难又有趣的问题。
    
    - – 
        
        For fields like psychology, philosophy, etc. we usually check if the rationale contains some reference to a book, paper or standard theories.  
        对于心理学、哲学等领域，我们通常会检查推理过程是否引用了书籍、论文或标准理论。
        
    - – 
        
        For fields like law, the question text can be adjusted with “as of 2024”. Make sure questions about law are time-bounded.  
        对于法律等领域，问题文本可调整为“截至 2024 年”。确保法律相关问题具有时效性。
        
    - – 
        
        Questions do not always need to be academic. A handful of movie, TV trivia, classics, history, art, or riddle questions in the dataset are OK.  
        问题不一定必须是学术性的。数据集中包含少量电影、电视冷知识、经典作品、历史、艺术或谜语类问题是可以接受的。
        
    - – 
        
        Trivia or complicated game strategy about chess, go, etc. are okay as long as they are difficult.  
        关于国际象棋、围棋等的冷知识或复杂游戏策略，只要难度足够高，也是可以接受的。
        
    - – 
        
        We generally want things that require a high level of human intelligence to figure out.  
        我们通常需要那些需要高水平人类智慧才能解答的内容。
        
    
- • 
    
    Questions should ask for something precise and have an objectively correct, univocal answer.  
    问题应要求精确的内容，并具有客观正确、明确的答案。
    
    - – 
        
        If there is some non-standard jargon for the topic/field, it needs to be explained.  
        如果涉及主题/领域中的非标准术语，则需加以解释。
        
    - – 
        
        Questions must have answers that are known or solvable.  
        问题必须有已知或可解的答案。
        
    - – 
        
        Questions should not be subjective or have personal interpretation.  
        问题不应是主观的或涉及个人解读。
        
    - – 
        
        Questions like “Give a proof of…”; “Explain why…”; “Provide a theory that explains…” are usually bad because they are not closed-ended and we cannot evaluate them properly. (Score 0)  
        诸如“给出……的证明”、“解释为何……”、“提出解释……的理论”这类问题通常不佳，因为它们并非封闭式问题，我们无法恰当地进行评估。（得分 0）
        
    - – 
        
        No questions about morality or what is ethical/unethical. (Score 0)  
        不涉及道德或伦理/非伦理问题。（得分 0）
        
    
- • 
    
    Questions should be original and not derived from textbooks or Google. (Score 0 if searchable on web)  
    问题应具有原创性，不得源自教科书或谷歌。（若能在网络上搜索到，得分为 0）
    
- • 
    
    Questions need to be in English. (Score 1 and ask for translation in the review if the question is written in a different language)  
    问题需以英文提出。（若问题以其他语言书写，得分为 1，并在评审中要求翻译）
    
- • 
    
    Questions should be formatted properly. (Score 1-3 depending on degree of revisions needed)  
    问题应格式规范。（根据所需修改程度，得分为 1-3）
    
    - – 
        
        Question with numerical answers should have results approximated to max 2-3 decimals.  
        对于需要数值答案的问题，结果应近似保留至最多 2-3 位小数。
        
    - – 
        
        Fix LaTeX formatting if possible. Models often get questions right after LaTeX formatting is added or improved.  
        尽可能修正 LaTeX 格式。模型通常在添加或改进 LaTeX 格式后能正确回答问题。
        
    - – 
        
        Questions that can be converted to text should be (converting images to text often helps models get them right).  
        可转换为文本的问题应进行转换（将图像转换为文本通常有助于模型正确解答）。
        
    

##### Other Tips  其他提示

- • 
    
    Please write detailed justifications and feedback. This is going out to the question submitter so please use proper language and be respectful.  
    请撰写详细的论证和反馈。这些内容将发送给问题提交者，因此请使用恰当的语言并保持尊重。
    
    - – 
        
        Explanations should include at least some details or reference. If the rationale is unclear or not detailed, ask in the review to expand a bit.  
        解释应至少包含一些细节或参考依据。如果论证不够清晰或详细，请在审核中要求对方稍作扩展。
        
    - – 
        
        Please check if the answer makes sense as a possible response to the question, but if you do not have knowledge/context, or if it would take more than 5 minutes to solve, that is okay.  
        请检查答案作为对问题的可能回应是否合理，但如果您缺乏相关知识/背景，或需要超过 5 分钟才能解决，这也没关系。
        
    
- • 
    
    Please prioritize questions with no reviews and skip all questions with more than 3 reviews.  
    请优先处理尚未审核的问题，并跳过所有已有超过 3 条审核的问题。
    
- • 
    
    Please double check that the model did actually answer the question wrong.  
    请务必仔细核对模型是否确实答错了问题。
    
    - – 
        
        Sometimes the exact match feature does not work well enough, and there are false negatives. We have to discard any exact match questions that a model got right.  
        有时精确匹配功能效果不佳，会出现误判。我们必须剔除所有模型答对的精确匹配问题。
        
    
- • 
    
    On the HLE dashboard, look at least 10 examples reviewed by the organizers before starting to review, and review the examples from training.  
    在 HLE 仪表板上，开始审核前至少查看 10 个由组织者审核过的示例，并仔细研究训练集中的案例。
    
- • 
    
    The average time estimated to review a question 3-5 minutes.  
    预计每个问题的平均审核时间为 3-5 分钟。
    
- • 
    
    Use a “-1 Unsure” review if the person submitting seems suspicious or if you’re not convinced their answer is right.  
    若提交者显得可疑，或您不确定其答案是否正确，请使用“-1 不确定”的评审。
    

|   |   |   |
|---|---|---|
|Score  分数|Scoring Guideline  评分指南|Description  描述|
|0|Discard  丢弃|The question is out of scope, not original, spam, or otherwise not good enough to be included in the HLE set and should be discarded.  <br>该问题超出范围、非原创、属于垃圾信息，或质量不足以纳入 HLE 数据集，应予以丢弃。|
|1|Major Revisions Needed  需要重大修订|Major revisions are needed for this question or the question is too easy and simple.  <br>该问题需要重大修订，或过于简单。|
|2|Some Revisions Needed  需要一些修改|Difficulty and expertise required to answer the question is borderline. Some revisions are needed for this question.  <br>问题的难度和所需专业知识处于临界水平。这个问题需要进行一些修改。|
|3|Okay  好的|The question is sufficiently challenging but the knowledge required is not graduate-level nor complex. Minor revisions may be needed for this question.  <br>问题具有足够的挑战性，但所需知识并非研究生水平或过于复杂。这个问题可能需要进行一些小的修改。|
|4|Great  优秀|The knowledge required is at the graduate level or the question is sufficiently challenging.  <br>所需知识达到研究生水平或问题具有足够挑战性。|
|5|Top-Notch  顶尖|Question is top-notch and perfect.  <br>问题质量顶尖且完美。|
|Unsure  不确定|-|Reviewer is unsure if the question fits the HLE guidelines, or unsure if the answer is right.  <br>审阅者不确定该问题是否符合 HLE 指南，或不确定答案是否正确。|

#### B.2.2Review Round 2  B.2.2 第二轮审阅

To thoroughly refine our dataset, we train a set of reviewers along with organizers to pick the best questions. These reviewers are identified by organizers from round 1 reviews as particularly high quality and thorough in their feedback. Different than the first round of reviews, reviewers are asked to grade both the question and look at feedback from round 1 reviewers. Organizers then approve questions based on reviewer feedback in this round. We employ a new rubric for this round below.  
为了彻底完善我们的数据集，我们与组织者一起训练了一组审阅者来挑选最佳问题。这些审阅者由组织者从第一轮审阅中识别出来，因其反馈质量特别高且全面。与第一轮审阅不同，审阅者被要求对问题进行评分，并查看第一轮审阅者的反馈。然后，组织者根据本轮审阅者的反馈来批准问题。我们在下方为本轮采用了新的评分标准。

|Score  分数|Scoring Guideline  评分指南|Description  描述|
|---|---|---|
|0|Discard  丢弃|The question is out of scope, not original, spam, or otherwise not good enough to be included in the HLE set and should be discarded.  <br>该问题超出范围、缺乏原创性、属于垃圾信息，或质量不足以纳入 HLE 数据集，应予以舍弃。|
|1|Not sure  不确定|Major revisions are needed for this question or you’re just unsure about the question. Please put your thoughts in the comment box and an organizer will evaluate this.  <br>该问题需要重大修改，或您对问题本身存疑。请在评论框中说明您的想法，组织者将对此进行评估。|
|2|Pending  待处理|You believe there are still minor revisions that are needed on this question. Please put your thoughts in the comment box and an organizer will evaluate this.  <br>你认为这道题仍需进行细微修改。请在评论区提出你的想法，组织者将对此进行评估。|
|3|Easy questions models got wrong  <br>模型答错的简单问题|These are very basic questions that models got correct or the question was easily found online. Any questions which are artificially difficult (large calculations needing a calculator, requires running/rendering code, etc.) should also belong in this category. The models we evaluate cannot access these tools, hence it creates an artificial difficulty bar. Important: “Found online” means via a simple search online. Research papers/journals/books are fine  <br>这些是非常基础的问题，模型要么答对了，要么问题很容易在网上找到。任何人为增加难度的问题（需要大量计算使用计算器、需要运行/渲染代码等）也应归入此类。我们评估的模型无法使用这些工具，因此这人为地提高了难度门槛。重要提示：“在网上找到”指的是通过简单的在线搜索。研究论文/期刊/书籍是可以接受的。|
|4|Borderline  临界问题|The question is not interesting OR The question is sufficiently challenging, but 1 or more of the models got the answer correct.  <br>该问题不够有趣，或者该问题具有足够挑战性，但有一个或多个模型给出了正确答案。|
|5|Okay to include in HLE benchmark  <br>可纳入 HLE 基准测试|Very good questions (usually has score of 3 in the previous review round). You believe it should be included in the HLE Benchmark.  <br>非常好的问题（通常在上一轮评审中得分为 3 分）。您认为应将其纳入 HLE 基准测试。|
|6|Top question in its category  <br>其类别中的首要问题|Great question (usually has a score of 4-5 in the previous review round), at a graduate or research level. Please note that “graduate level” is less strict for Non-STEM questions. For Non-STEM questions and Trivia, they are fine as long as they are challenging and interesting.  <br>极佳的问题（通常在上一轮评审中得分为 4-5 分），属于研究生或研究级别。请注意，对于非 STEM 问题，“研究生级别”的要求较为宽松。对于非 STEM 问题和琐事类问题，只要具有挑战性和趣味性即可。|

### B.3Subject List  B.3 科目列表

We allow question contributors to choose or declare a subject the author felt best suited their question. We present the top fifty most popular subjects in HLE below, although we note there are over a hundred subjects in the overall dataset.  
我们允许问题贡献者选择或声明他们认为最适合其问题的学科。以下列出了 HLE 中最受欢迎的五十个学科，尽管我们注意到整个数据集中包含超过一百个学科。

Mathematics, Physics, Computer Science, Chemistry, Applied Mathematics, Trivia, Electrical Engineering, Biology, Linguistics, Medicine, Genetics, History, Economics, Ecology, Artificial Intelligence, Musicology, Philosophy, Neuroscience, Law, Art History, Biochemistry, Astronomy, Classics, Chess, Chemical Engineering, Microbiology, Classical Ballet, Materials Science, Poetry, Quantum Mechanics, Aerospace Engineering, Civil Engineering, Mechanical Engineering, Geography, Robotics, Data Science, Molecular Biology, Statistics, Immunology, Education, Logic, Computational Biology, Psychology, English Literature, Machine Learning, Puzzle, Cultural Studies, Marine Biology, Archaeology, and Biophysics.  
数学、物理学、计算机科学、化学、应用数学、常识问答、电气工程、生物学、语言学、医学、遗传学、历史学、经济学、生态学、人工智能、音乐学、哲学、神经科学、法学、艺术史、生物化学、天文学、古典学、国际象棋、化学工程、微生物学、古典芭蕾、材料科学、诗歌、量子力学、航空航天工程、土木工程、机械工程、地理学、机器人学、数据科学、分子生物学、统计学、免疫学、教育学、逻辑学、计算生物学、心理学、英国文学、机器学习、谜题、文化研究、海洋生物学、考古学和生物物理学。

## Appendix CEvaluation  附录 C 评估

### C.1Prompts  C.1 提示

#### C.1.1Evaluation  C.1.1 评估

We use the following system prompt for evaluating LLMs on multiple-choice questions:  
我们使用以下系统提示来评估 LLMs 在多项选择题上的表现：

Your response should be in the following format:

Explanation: {your explanation for your answer choice}

Answer: {your chosen answer}

Confidence: {your confidence score between 0% and 100% for your answer}

We use the following system prompt for evaluating LLMs on exact-match questions:  
我们使用以下系统提示来评估 LLMs 在精确匹配题上的表现：

Your response should be in the following format:

Explanation: {your explanation for your final answer}

Exact Answer: {your succinct, final answer}

Confidence: {your confidence score between 0% and 100% for your answer}

We use the following system prompt to judge the model answers against the correct answers for our evaluations in [Table˜1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4.T1 "In Calibration Error. ‣ 4.2 Quantitative Results ‣ 4 Evaluation ‣ Humanity’s Last Exam"). We used gpt-4o-2024-08-06 with structured decoding enabled to get an extracted_final_answer, reasoning, correct, confidence extraction for each output.  
我们使用以下系统提示，根据正确答案来评判模型答案，用于表˜1 中的评估。我们使用了 gpt-4o-2024-08-06 模型并启用了结构化解码，以获取每个输出的 extracted_final_answer、reasoning、correct 和 confidence 提取结果。

Judge whether the following [response] to [question] is correct or not

based on the precise and unambiguous [correct_answer] below.

[question]: {question}

[response]: {response}

Your judgement must be in the format and criteria specified below:

extracted_final_answer: The final exact answer extracted from the

[response]. Put the extracted answer as ’None’ if there is no exact, final

answer to extract from the response.

[correct_answer]: {correct_answer}

reasoning: Explain why the extracted_final_answer is correct or incorrect

based on [correct_answer], focusing only on if there are meaningful

differences between [correct_answer] and the extracted_final_answer. Do

not comment on any background to the problem, do not attempt to solve

the problem, do not argue for any answer different than

[correct_answer], focus only on whether the answers match.

correct: Answer ’yes’ if extracted_final_answer matches the

[correct_answer] given above, or is within a small margin of error for

numerical problems. Answer ’no’ otherwise, i.e. if there if there is any

inconsistency, ambiguity, non-equivalency, or if the extracted answer is

incorrect.

confidence: The extracted confidence score between 0% and 100% from

[response]. Put 100 if there is no confidence score available.

### C.2Text-Only Results  C.2 纯文本结果

|Model|Accuracy (%) ↑  准确率 (%) ↑|Calibration Error (%) ↓  <br>校准误差（%） ↓|
|---|---|---|
|GPT-4o|2.9|90.4|
|Grok 2|3.9|92.5|
|Claude 3.5 Sonnet|4.2|87.0|
|Gemini 1.5 Pro|4.8|91.1|
|Gemini 2.0 Flash Thinking  <br>双子座 2.0 闪电思维|5.9|92.1|
|o1|8.9|92.0|
|DeepSeek-R1|9.4|81.8|

Table 2:Accuracy and RMS calibration error of models from [Table˜1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S4.T1 "In Calibration Error. ‣ 4.2 Quantitative Results ‣ 4 Evaluation ‣ Humanity’s Last Exam") on the text-only questions of HLE, representing 90% of the public set.  
表 2：表˜1 中模型在 HLE 纯文本问题上的准确率和 RMS 校准误差，占公开数据集的 90%。

### C.3Non-Reasoning Model Token Counts  
C.3 非推理模型的标记数量统计

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2501.14249/assets/x6.png)

Figure 6:Average output token counts of non-reasoning models.  
图 6：非推理模型的平均输出标记数量。

### C.4Model Versions  C.4 模型版本

|Model|Version  版本|
|---|---|
|GPT-4o|gpt-4o-2024-11-20|
|Grok 2|grok-2-latest|
|Claude 3.5 Sonnet|claude-3-5-sonnet-20241022|
|Gemini 1.5 Pro|gemini-1.5-pro-002|
|Gemini 2.0 Flash Thinking  <br>双子座 2.0 闪电思维|gemini-2.0-flash-thinking-exp-1219|
|o1|o1-2024-12-17|
|DeepSeek-R1|January 20, 2025 release  <br>2025 年 1 月 20 日发布|

Table 3:Evaluated model versions. All models use temperature 0 when configurable.  
表 3：评估模型版本。所有模型在可配置时均使用温度参数 0。

### C.5Benchmark Difficulty Comparison  
C.5 基准难度对比

In [Figure˜1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#S1.F1 "In 1 Introduction ‣ Humanity’s Last Exam"), we evaluate the accuracy of all models on HLE using our zero-shot chain-of-thought prompts ([Section˜C.1.1](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#A3.SS1.SSS1 "C.1.1 Evaluation ‣ C.1 Prompts ‣ Appendix C Evaluation ‣ Humanity’s Last Exam")). On prior benchmarks, we list our sources here.  
在图˜1 中，我们使用零样本思维链提示（第˜C.1.1 节）评估所有模型在 HLE 上的准确率。关于先前基准测试，我们在此列出数据来源。

For GPT-4o and o1-preview, we report zero-shot, chain-of-thought results from OpenAI found at [https://github.com/openai/simple-evals](https://github.com/openai/simple-evals).  
对于 GPT-4o 和 o1-preview 模型，我们报告了 OpenAI 在 https://github.com/openai/simple-evals 上公布的零样本思维链结果。

For Gemini 1.5 Pro, we report 5-shot MMLU Team et al. [[49](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib49)] and other results from [Google’s reported results here](https://developers.googleblog.com/en/updated-gemini-models-reduced-15-pro-pricing-increased-rate-limits-and-more/).  
对于 Gemini 1.5 Pro 模型，我们报告了 MMLU 团队等人[49]的 5 样本测试结果，以及谷歌在此处公布的其他结果。

For Claude 3.5 Sonnet, we report 0-shot chain-of-thought results from Anthropic [[4](https://ar5iv.labs.arxiv.org/html/2501.14249?_immersive_translate_auto_translate=1#bib.bib4)].  
对于 Claude 3.5 Sonnet 模型，我们报告了 Anthropic[4]公布的零样本思维链结果。

[◄](https://ar5iv.labs.arxiv.org/html/2501.14247) [![ar5iv homepage](https://ar5iv.labs.arxiv.org/assets/ar5iv.png)](https://ar5iv.labs.arxiv.org/) [Feeling  ◄ ![ar5iv homepage](https://ar5iv.labs.arxiv.org/assets/ar5iv.png) 感受  
lucky?](https://ar5iv.labs.arxiv.org/feeling_lucky) [](https://ar5iv.labs.arxiv.org/land_of_honey_and_milk)[Conversion  幸运？转换  
report](https://ar5iv.labs.arxiv.org/log/2501.14249) [Report  报告报告  
an issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2501.14249) [View original  一个问题查看原文  
on arXiv](https://arxiv.org/abs/2501.14249)[►](https://ar5iv.labs.arxiv.org/html/2501.14250)  在 arXiv 上 ►

[Copyright](https://arxiv.org/help/license) [Privacy Policy](https://arxiv.org/help/policies/privacy_policy) 

Generated on Wed Feb 5 15:55:25 2025 by [LaTeXML![Mascot Sammy](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAOCAYAAAD5YeaVAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9wKExQZLWTEaOUAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1Q72QlbgAAAdpJREFUKM9tkL+L2nAARz9fPZNCKFapUn8kyI0e4iRHSR1Kb8ng0lJw6FYHFwv2LwhOpcWxTjeUunYqOmqd6hEoRDhtDWdA8ApRYsSUCDHNt5ul13vz4w0vWCgUnnEc975arX6ORqN3VqtVZbfbTQC4uEHANM3jSqXymFI6yWazP2KxWAXAL9zCUa1Wy2tXVxheKA9YNoR8Pt+aTqe4FVVVvz05O6MBhqUIBGk8Hn8HAOVy+T+XLJfLS4ZhTiRJgqIoVBRFIoric47jPnmeB1mW/9rr9ZpSSn3Lsmir1fJZlqWlUonKsvwWwD8ymc/nXwVBeLjf7xEKhdBut9Hr9WgmkyGEkJwsy5eHG5vN5g0AKIoCAEgkEkin0wQAfN9/cXPdheu6P33fBwB4ngcAcByHJpPJl+fn54mD3Gg0NrquXxeLRQAAwzAYj8cwTZPwPH9/sVg8PXweDAauqqr2cDjEer1GJBLBZDJBs9mE4zjwfZ85lAGg2+06hmGgXq+j3+/DsixYlgVN03a9Xu8jgCNCyIegIAgx13Vfd7vdu+FweG8YRkjXdWy329+dTgeSJD3ieZ7RNO0VAXAPwDEAO5VKndi2fWrb9jWl9Esul6PZbDY9Go1OZ7PZ9z/lyuD3OozU2wAAAABJRU5ErkJggg==)](http://dlmf.nist.gov/LaTeXML/)