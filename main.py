import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



st.set_page_config(
    page_title="Color Choice",
    page_icon="🎨",
)


def colored_histogram(values, colors):
    n_bins = len(values)

    fig, ax = plt.subplots()
    for i in range(n_bins):
        ax.bar(i, 1, color=colors[i], edgecolor='white')

    ax.set_xlim(0, n_bins)
    ax.set_ylim(0, 1)
    ax.axis('off')  # Turn off the axis

    return fig


@st.cache_data
def get_color_history():
    return []


def main():

    st.title('_Soul_:blue[_Sketch_]')
    st.header('Select your mood for the day', 'blue')

    r1 = st.button(':red[RED]')
    r2 = st.button(':green[GREEN]')
    r3 = st.button(':violet[VIOLET]')
    r4 = st.button(':grey[GREY]')
    r5 = st.button(':orange[ORANGE]')
    r6 = st.button(':blue[BLUE]')

    color = ''
    colors = get_color_history()

    if r1:
        color = 'RED'
    elif r2:
        color = 'GREEN'
    elif r3:
        color = 'VIOLET'
    elif r4:
        color = 'GREY'
    elif r5:
        color = 'ORANGE'
    elif r6:
        color = 'BLUE'

    default_string = 'You didnt select an emotional color for today, please select one on the previous page :D'
    red_string = f'Your emotional color today leans towards red, signifying a propensity for _:{color.lower()}[ANGER]_, its crucial to prioritize the management of this intense emotion for the sake of your well-being and relationships. When anger surfaces, take a deliberate pause, focusing on deep, slow breaths to calm your nervous system and allow for rational thinking. Identify specific triggers that lead to your _:{color.lower()}[ANGER]_, enabling you to anticipate and navigate emotional responses more effectively. Express your feelings calmly using "I" statements, steering away from blame. Seek to understand the root cause of your _:{color.lower()}[ANGER]_, addressing underlying issues or unmet needs. Cultivate empathy by considering the perspectives and motivations of others, fostering a more nuanced understanding. Channel your _:{color.lower()}[ANGER]_ into constructive outlets such as physical activities or creative pursuits. Establish clear boundaries to prevent situations that commonly trigger _:{color.lower()}[ANGER]_, communicating these boundaries assertively yet respectfully. Hone conflict resolution skills, emphasizing problem-solving over escalation. If _:{color.lower()}[ANGER]_ persists, seek support from friends, family, or a mental health professional who can offer valuable insights and coping strategies. Explore mindfulness and relaxation techniques, such as meditation or yoga, to stay present and reduce overall stress levels. After moments of _:{color.lower()}[ANGER]_, reflect on the situation, considering what triggered your emotions and how you might handle similar situations differently in the future. Remember, managing _:{color.lower()}[ANGER]_ is an ongoing process, and progress takes time. Be patient with yourself, celebrate small victories, and if needed, seek professional guidance for continued personal growth and emotional well-being.'
    green_string = f'Your emotional color today leans towards green, representing a tendency towards _:{color.lower()}[JOY]_, its essential to cultivate and nurture this positive emotion for your overall well-being. When you experience joy, fully embrace and savor those moments. Allow yourself to be present and appreciate the positive aspects of your life. Identify activities, people, or environments that consistently bring you _:{color.lower()}[JOY]_ and make an effort to incorporate them into your routine. Practice gratitude regularly, acknowledging and expressing thanks for the positive elements in your life. Share your _:{color.lower()}[JOY]_ with others, as spreading joy can create a positive ripple effect. Cultivate a positive mindset by focusing on solutions and opportunities rather than dwelling on challenges. Engage in activities that bring a sense of fulfillment and purpose, contributing to your overall _:{color.lower()}[JOY]_. Prioritize self-care, ensuring that you allocate time for activities that recharge and rejuvenate you. Surround yourself with supportive and positive individuals who uplift and inspire you. Foster a sense of connection and belonging, as social relationships play a significant role in sustaining _:{color.lower()}[JOY]_. Reflect on your achievements and milestones, celebrating both small and large successes. Remember that _:{color.lower()}[JOY]_ is a journey, and finding joy in the little moments contributes to a more fulfilling and balanced life.'
    violet_string = f'Your emotional color today tends towards violet, symbolizing _:{color.lower()}[SADNESS]_, its crucial to approach this emotion with compassion and proactive strategies for well-being. When _:{color.lower()}[SADNESS]_ arises, allow yourself the space to acknowledge and process these feelings without judgment. Take time for self-reflection, seeking to understand the root causes of your _:{color.lower()}[SADNESS]_ and any patterns or triggers that may contribute to it. Consider expressing your emotions through creative outlets like art or writing to provide a healthy release. Reach out to supportive friends, family, or a mental health professional to share your feelings and gain perspective. Engage in activities that bring comfort and solace, focusing on self-care practices that resonate with you. Establish a routine that includes positive habits and moments of joy, even during periods of _:{color.lower()}[SADNESS]_. Practice mindfulness and relaxation techniques, such as meditation, to create a sense of calm and centeredness. Remember that seeking help is a sign of strength, and professional support can offer valuable insights and coping strategies. Cultivate resilience by embracing the ebb and flow of emotions, understanding that _:{color.lower()}[SADNESS]_ is a natural part of the human experience. In moments of vulnerability, be kind to yourself and allow the necessary time for healing and renewal. Remember that you are not alone, and reaching out for support is an empowering step towards emotional well-being.'
    grey_string = f'Your emotional color today tends towards grey, symbolizing _STRESS_, its essential to approach this emotion with mindful strategies to alleviate and manage _STRESS_ for your overall well-being. When _STRESS_ arises, acknowledge it without judgment and recognize that it is a common part of life. Take intentional breaks throughout the day to practice deep breathing or mindfulness, creating moments of calm amidst the chaos. Identify the specific sources of _STRESS_ in your life, whether they are related to work, relationships, or other factors, and develop practical steps to address them. Consider creating a structured daily routine to provide a sense of predictability and control. Delegate tasks when possible, recognizing that you dont have to handle everything on your own. Prioritize self-care, incorporating activities that bring relaxation and joy into your daily life. Engage in regular physical activity, as exercise is a powerful _STRESS_ reliever. Seek social support from friends, family, or colleagues, sharing your feelings and concerns to gain perspective and assistance. Set realistic goals and expectations for yourself, understanding that its okay to say no and establish boundaries. Practice time management techniques to prioritize tasks and reduce feelings of overwhelm. Consider learning and practicing _STRESS_ management techniques such as meditation or yoga to promote a sense of inner peace. If _STRESS_ becomes overwhelming, consider seeking professional support from a mental health professional who can provide guidance and coping strategies. Remember that managing _STRESS_ is an ongoing process, and small, consistent changes can contribute to a more balanced and resilient life.'
    orange_string = f'Your emotional color today tends towards orange, indicating _:{color.lower()}[ANXIETY]_, its crucial to approach this emotion with effective strategies to alleviate and manage _:{color.lower()}[ANXIETY]_ for your overall well-being. When _:{color.lower()}[ANXIETY]_ arises, acknowledge it without judgment and recognize that it is a common aspect of human experience. Implement grounding techniques, such as focused breathing or mindfulness, to create a sense of presence in the moment. Identify specific triggers of your _:{color.lower()}[ANXIETY]_, whether they relate to work, relationships, or other aspects of life, and develop practical steps to address them. Establish a routine that provides structure and predictability, which can contribute to a sense of control. Incorporate relaxation activities into your daily life, such as engaging in hobbies or spending time in nature, to promote a calming effect. Seek support from friends, family, or colleagues, sharing your feelings and concerns to gain perspective and assistance. Focus on realistic goals and expectations, recognizing that perfection is not achievable, and its okay to set boundaries. Engage in regular physical activity, as exercise has been shown to be beneficial for reducing _:{color.lower()}[ANXIETY]_. Consider exploring _:{color.lower()}[ANXIETY]_ management techniques, such as meditation or deep-breathing exercises, to foster a sense of tranquility. If _:{color.lower()}[ANXIETY]_ becomes overwhelming, consider seeking professional support from a mental health professional who can provide guidance and coping strategies. Remember that managing _:{color.lower()}[ANXIETY]_ is an ongoing process, and incorporating small, consistent changes can contribute to a more balanced and resilient life.'
    blue_string = f'If your emotional color tends towards blue, indicating a predisposition towards _:{color.lower()}[TRANQUILITY]_, its important to foster and embrace this serene emotion for your overall well-being. When you experience _:{color.lower()}[TRANQUILITY]_, savor the tranquility of the moment, allowing it to wash over you. Engage in activities that promote relaxation and peace, such as meditation or gentle stretching exercises. Create a calming environment in your daily life, incorporating soothing colors and elements that contribute to a sense of serenity. Establish routines that provide stability and predictability, contributing to a calm and organized mindset. Prioritize self-care, making time for activities that bring you joy and relaxation. Seek out nature or bodies of water, as the calming effect of blue is often associated with the sky and the ocean. Practice deep-breathing exercises to maintain a steady and calm presence in challenging situations. Surround yourself with supportive and positive influences, fostering an environment that promotes tranquility. Consider mindful practices, such as journaling or gratitude exercises, to center your thoughts and promote a sense of calm reflection. Embrace a healthy work-life balance, ensuring that you allocate time for both productivity and relaxation. Remember that _:{color.lower()}[TRANQUILITY]_ is a valuable state of being, and cultivating it is an ongoing process that contributes to a more balanced and harmonious life.'

    if color != '':
        st.title(f'Your emotional color of the day is _:{color.lower()}[{color}]_')

    if color == 'RED':
        st.write(red_string)
    elif color == 'GREEN':
        st.write(green_string)
    elif color == 'VIOLET':
        st.write(violet_string)
    elif color == 'GREY':
        st.write(grey_string)
    elif color == 'ORANGE':
        st.write(orange_string)
    elif color == 'BLUE':
        st.write(blue_string)

    if color != '':
        colors.append(color)

    st.pyplot(colored_histogram(range(len(colors)), colors))


if __name__ == "__main__":
    main()
