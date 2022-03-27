from stack import Stack

def check_sequence(input_str: str):
    st = Stack([])
    is_good = True
    for i in input_str:
        if i in '([{':
            st.push(i)
        if i in ')]}':
            if st.is_empty():
                is_good = False
                break
            if st.peek() == '(' and i == ')':
                st.pop()
            elif st.peek() == '{' and i == '}':
                st.pop()
            elif st.peek() == '[' and i == ']':
                st.pop()

            else:
                is_good = False
                break
    if is_good and st.size() == 0:
        print('Сбалансированно')
    else:
        print('Несбалансированно')

if __name__ == '__main__':
    check_sequence('}{}')
