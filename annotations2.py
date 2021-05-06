#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:39:48 2021

@author: santealtamura
"""

import csv

"""
Altamura       :	coppie nell'intervallo 201-250

"""

with open('annotations/annotations2.tsv', 'wt') as out_file:
    
    #processo di annotazione manuale
    ##Term1 Term2 BS1 BS2 Terms_in_BS1 Terms_in_BS2
    
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['terremoto', 'scossa', 'bn:00029448n','bn:00029441n','sisma,attività sismica,tremito','microsisma,microsismo'])
    tsv_writer.writerow(['patrimonio', 'azione', 'bn:00080746n','bn:00070912n','ricchezza,ricco,facoltoso','compartecipazione,quota'])
    tsv_writer.writerow(['ebreo', 'Gerusalemme', 'bn:00043492n','bn:00015555n','israelita,giudeo','Gerico'])
    tsv_writer.writerow(['nuvolosità', 'previsione', 'bn:00020002n','bn:00004638n','nube,nembo','anticipazione,predizione,vaticinio'])
    tsv_writer.writerow(['dizionario', 'enciclopedia', 'bn:00026967n','bn:00024746n','vocabolario,lessico,calepino','opera di consultazione'])
    tsv_writer.writerow(['zecca', 'museo', 'bn:00055225n','bn:00056426n','monete','manufatti,scienza'])
    tsv_writer.writerow(['sedia', 'sgabello', 'bn:00017515n','bn:00074427n','seggiola,gamba della sedia','panchetto'])
    tsv_writer.writerow(['spagnolo', 'umidità', 'bn:00073092n','bn:00045190n','Lingua spagnola','vapore acqueo'])
    tsv_writer.writerow(['lattina', 'bottiglia', 'bn:00072586n','bn:00012339n','bibite','contenitore d alluminio','vetro,liquidi'])
    tsv_writer.writerow(['mosca', 'formica', 'bn:13319918n','bn:00004458n','insetto','insetto'])
    tsv_writer.writerow(['mito', 'satira', 'bn:00056669n','bn:00013998n','racconto mitologico','caricatura'])
    tsv_writer.writerow(['coda', 'Boeing 747-200', 'bn:00030590n','bn:03226093n','aeromobile,impennaggio','aereo'])
    tsv_writer.writerow(["opera d'arte", 'artista', 'bn:00081581n','bn:00006182n','creazione artistica','attività artistica'])
    tsv_writer.writerow(['NATO', 'alleanza', 'bn:00056978n','bn:03544293n','organizzazione internazionale','associazione,patto'])
    tsv_writer.writerow(['re', 'sovrano', 'bn:00024097n','bn:00024097n','regnante','regnante'])
    tsv_writer.writerow(['ritmo', 'cadenza', 'bn:00009396n','bn:00014520n','tempo','teoria musicale,composizione'])
    tsv_writer.writerow(['Alexander Fleming', 'penicillina', 'bn:00002616n','bn:00061363n','medico,farmacologo','antibiotici'])
    tsv_writer.writerow(['flauto', 'musica', 'bn:00035477n','bn:00056443n','aerofoni labiali','melomane'])
    tsv_writer.writerow(['airone cenerino', 'lago', 'bn:16449236n','bn:00049709n','uccello','massa di acqua'])
    tsv_writer.writerow(['viscosità', 'spruzzo', 'bn:00080092n','bn:00073618n','vischiosità,grandezza fisica','acqua'])
    tsv_writer.writerow(['hardware', 'case', 'bn:00021480n','bn:00262368n','materiale informatico','informatica,computer'])
    tsv_writer.writerow(['anello', 'fidanzamento', 'bn:00008287n','bn:00010152n','gioiello','fidanzata,promessa sposa,promessa'])
    tsv_writer.writerow(['latino', 'tedesco', 'bn:00050161n','bn:00040293n','Lingua latina','Lingua tedesca'])
    tsv_writer.writerow(['classe operaia', 'fabbrica', 'bn:00049570n','bn:00032675n','classe lavoratrice,lavoro,lavoranti','stabilimento,manifattura,impianto'])
    tsv_writer.writerow(['Shakespeare', 'Dickens', 'bn:00008556n','bn:00017842n','drammaturgo,poeta inglese','scrittore,giornalista,reporter'])
    tsv_writer.writerow(['banconota', 'prete', 'bn:00008375n','bn:00057892n','biglietto di banca,biglietto,cambiale','religione'])
    tsv_writer.writerow(['strumento', 'lavoro', 'bn:00077585n','bn:14959529n','utensile,arnese','attività produttiva,compenso'])
    tsv_writer.writerow(['cinghiale nano', 'suidi', 'bn:03100066n','bn:00033468n','suide','maiali'])
    tsv_writer.writerow(['suffragio', 'uscita', 'bn:00067845n','bn:00032243n','diritto di voto','andare fuori'])
    tsv_writer.writerow(['stella', 'luminosità', 'bn:00073964n','bn:14292145n','astro,sole','stella,energia elettromagnetica,astronomia'])
    tsv_writer.writerow(['trota', 'chitarra', 'bn:00078435n','bn:00042150n','pesce','strumento musicale,corde'])
    tsv_writer.writerow(['dollaro', 'milionario', 'bn:00079129n','bn:00055058n','biglietto verde,dollaro USA','patrimonio'])
    tsv_writer.writerow(['cifra', 'numero', 'bn:00025702n','bn:00058285n','simbolo,numeri,sistema numerico','grandezze,ente astratto'])
    tsv_writer.writerow(['burrasca', 'coperta', 'bn:00074458n','bn:00011119n','bufera,temporale,fortunale','coltre,copriletto'])
    tsv_writer.writerow(['Obama', 'Clinton', 'bn:03330021n','bn:00010400n','politico,presidente','presidente'])
    tsv_writer.writerow(['personaggio secondario', 'film', 'bn:00206836n','bn:00034481n','personaggio,narrazione','produzione cinematografica'])
    tsv_writer.writerow(['Juventus', 'Bayern Monaco', 'bn:00876765n','bn:00963795n','Torino,società calcistica','società polisportiva tedesca,Bundesliga'])
    tsv_writer.writerow(['cambiamento climatico', 'precipitazione', 'bn:00019782n','bn:00028483n','cambiamento del clima,mutamento climatico','precipitazione atmosferica'])
    tsv_writer.writerow(['IA', 'batteria', 'bn:00002150n','bn:00009064n','intelligenza artificiale','pila elettrica,accumulatore'])
    tsv_writer.writerow(['capolavoro', 'Gioconda', 'bn:00053738n','bn:03571983n','opera ben riuscita','dipinto'])
    tsv_writer.writerow(['crimine', 'aggressione', 'bn:00023807n','bn:00002015n','reato,delitto,misfatto,fattaccio','aggressività,atto di violenza'])
    tsv_writer.writerow(['incoronazione', 'acqua', 'bn:00022800n','bn:00042379n','investitura,coronazione,incoronamento','H2O,composto chimico,atomi di idrogeno'])
    tsv_writer.writerow(['spareggio', 'pallacanestro', 'bn:00062962n','bn:00008889n','play-off','basket,basketball,cestismo'])
    tsv_writer.writerow(['forze armate', 'difesa', 'bn:00005732n','bn:00025878n','forze militari,militari','azione militare,difendere'])
    tsv_writer.writerow(['lago', 'nuvola', 'bn:00049709n','bn:00020002n','massa di acqua','nube,nembo'])
    tsv_writer.writerow(['monastero', 'doccia', 'bn:13460974n','bn:00071324n','monaci,monache,religioni','acqua,strumento,persona'])
    tsv_writer.writerow(['lingua madre', 'lingua', 'bn:00034782n','bn:00049911n','madrelingua,lingua materna','linguaggio,parlare,parlata'])
    tsv_writer.writerow(['porto', 'incarto', 'bn:00063640n','bn:00060120n','litorale marittimo,struttura,riva','imballo'])
    